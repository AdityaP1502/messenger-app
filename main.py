import sys

from src.client.client import Client
from src.client.connection import Connection
from src.client.writer import Writer
from src.client.receiver import Receiver

if __name__ == "__main__":
  assert len(sys.argv) > 1, "Usage python client.py [username]"
  username = sys.argv[1]
  
  client = Client(username)
  conn = Connection(client)
  
  # create a writer thread
  writer_t = Writer(name="writer_thread", args=(client, ), daemon = True)
  writer_t.start()
  
  # connect and register channel
  conn.connect_to_socket(hostname="localhost", port=8080)
  
  receiver_t = Receiver(name="connection_thread", target=Receiver.receive, args=(client.message_buffer, conn, ), daemon = True)
  receiver_t.start()
    
  conn.register_channel()
  action = ""
  
  if not conn.running:
    print("Login failed. Please try again!")
    sys.exit(-1)
    
  while (action != "TERMINATE"):
    client.state.value = 0
    action = input("input action:").upper()
    
    if not conn.running:
      break
      
    if action == "SENDMESSAGE":
      client.state.value = 1
      recipient = input("recipient:")
      
      if not conn.running:
        break
        
      client.state.value = 2
      message = input("message:")
      
      if not conn.running:
        break
      
      client.send_message(recipient=recipient, message=message, conn=conn)
    
    elif action == "TERMINATE":
      print("Terminating connection!")
      
    else:
      print("Wrong action")
      continue
    
