import sys
import socket
import errno
from time import sleep
from threading import Thread
from typing import Any, Callable, Iterable, Mapping


class Receiver(Thread):
  EOF = "\n"
  
  def __init__(self, group: None = None, target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., kwargs: Mapping[str, Any] | None = None, *, daemon: bool | None = None) -> None:
    super().__init__(group, target, name, args, kwargs, daemon=daemon)
    
  def start(self) -> None:
    return super().start()
    
  def join(self, timeout: float | None = None) -> None:
    return super().join(timeout)
  
  @staticmethod
  def receive(buffer, conn):
    while not conn.has_registered or conn.running:
      try:
            msg = conn.socket.recv(4096)
      except socket.error as e:
            err = e.args[0]
            if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
                sleep(1)
                continue
            else: 
                sys.stdout.write('\r{}\n'.format(e))
                print("Error occured\npress ENTER to exit")
                conn.running = False
                break
      else:
            incoming_response = msg.decode('UTF-8')
            # current_prompt = self.client.get_current_prompt()
            
            # if current_prompt == '':
            #   break
            
            packets = incoming_response.split(Receiver.EOF)
            
            for packet in packets[:-1]:
              Receiver.process_incoming_response(packet, conn, buffer)
            # sys.stdout.write('\rGetting {}\n{}'.format(msg, current_prompt))
  
  @staticmethod
  def parse_message(packet : str):
    """pass the packet that is received
    """
    
    restype, payload = packet.split(";", 1)
    _, restype_value = restype.split("=", 1)
    _, payload_value = payload.split("=", 1)
    
    return restype_value, payload_value 
  
  @staticmethod
  def process_incoming_response(packet : str, conn, buffer):
    """process response
    """
    restype, payload = Receiver.parse_message(packet)
  
    if restype == "OK":
      _, uid_value = payload.split("=", 1)
      try:
        uid_integer = int(uid_value)
        conn.request_status[uid_integer] = "OK"
        conn.request_state[uid_integer] = 0
        
      except Exception as e:
        print(e)
        uid_integer = -1
        return

    elif restype == "MESSAGE":
      parsedResponse = payload.split(";", 2)
      data = []
      
      for field in parsedResponse:
        _, value = field.split("=", 1)
        data.append(value)
        
      buffer.put(data)
    
    elif restype == "ERROR":
      error_field, uid_field = payload.split(";", 2)
      
      _, uid = uid_field.split("=", 2)
      _, err = error_field.split("=", 2)
      
      try:
        uid_integer = int(uid)
        conn.request_status[uid_integer] = err
        conn.request_state[uid_integer] = 0
        
      except Exception as e:
        print(e)
        uid_integer = -1
        return
      
      
  
    
    