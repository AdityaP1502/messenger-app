import sys

from client import Client
from connection import Connection
from ui.cli.writer import Writer
from receiver import Receiver

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please specified the username!")
        print("Usage python main.py [username]")
        sys.exit(-1)
    
    username = sys.argv[1]

    client = Client(username)
    conn = Connection(client)

    # create a writer thread
    writer_t = Writer(name="writer_thread", args=(client, ), daemon=True)
    writer_t.start()

    # connect and register channel
    try:
        conn.connect_to_socket(hostname="localhost", port=8080)
    except Exception as e:
        print("Cant connect to server!")
        print(e)
        sys.exit(-1)        
        
    receiver_t = Receiver(name="connection_thread",
                          target=Receiver.receive,
                          args=(
                              client.message_buffer,
                              conn,
                          ),
                          daemon=True)
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

            client.send_message(recipient=recipient,
                                message=message,
                                conn=conn)

        elif action == "TERMINATE":
            print("Terminating connection!")

        else:
            print("Wrong action")
            continue
