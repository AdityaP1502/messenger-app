import socket
import sys
import errno
from time import sleep
import signal
import threading
from multiprocessing import Queue

from src.client.receiver import Receiver

REQUEST_MAXSIZE = 256

class Connection():
  def __init__(self, client) -> None:
    self.socket = None
    self.__client = client # a client object that use this connection 
    self.is_secure = False
    self.running = False # the state of the connection
    self.has_registered = False 
    self.request_status = ["" for i in range(REQUEST_MAXSIZE)]
    self.request_state = [0 for i in range(REQUEST_MAXSIZE)]
    self.request_number = -1
  
  def send(self, data : str):
    # send a request/data to the server
    # encrypt if use secure_connection
    
    self.request_number = (self.request_number + 1) % REQUEST_MAXSIZE
    
    if self.request_state[self.request_number] == 1:
      # wait until the request is finished
      while self.request_state[self.request_number] == 1:
        continue
    
    data = "uid={};{}".format(self.request_number, data) + '\n' 
    
    if self.is_secure:
      pass
    
    self.socket.send(data.encode())
    
    status = self.__wait_for_response(self.request_number)
    return status
  
  def __wait_for_response(self, uid : int):
    
    while self.request_status[uid] == "":
      continue
      
    self.request_status[uid] = ""
    self.request_state[uid] = 0
    
    return self.request_status[uid]
      
  def __init_receiver(self):
    t = threading.Thread(target=self.__receive, daemon=True)
    t.start()
    return t
  
  def connect_to_socket(self, hostname: str, port : int):
    """Establish a socket connection to the server
    """
    # create a socket
    
    try:
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
      return -1, "socket creation failed with error {}".format(err)
    
    try:
      host_ip = socket.gethostbyname("localhost")
    except socket.error as err:
      return -1, "There was an error resolving the hostname"
    
    self.socket.connect((host_ip, port))
    self.socket.setblocking(0)
    
  def register_channel(self):
    return self.check_in(self.__client.username)
    
  def check_in(self, username : str):
    """Register the user username to the socket
    """
    
    message = "reqtype=CHECKIN;payload=username={}".format(username)
    
    status = self.send(message)
    
    if status == "OK":
      self.has_registered = True
      self.running = True
      return 0
    
    else:
      return -1

  def secure_connection(self):
    """Establish TLS connection to the server
    """
    pass
  
  def terminate_connection(self, username : str):
    """close the connection the server
    """
    
    message = "reqtype=TERMINATE;payload=username={}".format(username)
    status = self.send(message)
    
    if status == "OK":
      self.socket.close()
      self.running = False
      return 0
    
    return -1