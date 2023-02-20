from multiprocessing import Value, Queue
from connection import Connection
class Client():

    def __init__(self, username: str) -> None:
        self.username = username
        self.state = Value("i", 0)
        self.message_buffer = Queue(maxsize=100)

    def get_state(self):
        """get the state of the client

    Returns:
        state : int
    """

        with self.state.get_lock():
            return self.state.value

    def get_current_prompt(self):
        """return the current prompt

    Returns:
        str : current prompt for the user input
    """
        state = self.get_state()

        if state == 0:
            return 'input action:'

        elif state == 1:
            return 'recipient:'

        elif state == 2:
            return 'message:'

        return ''

    def send_message(self, message: str, recipient: str, conn: Connection):
        """Send a message to recipient via the connection made with the server

    Args:
        message (str): Message to be sent
        recipient (str): the recipient of the message
        conn (Connection) : Connection to the channel
    """

        message = "reqtype=SENDMESSAGE;payload=sdr={};rcpt={};message={}".format(
            self.username, recipient, message)

        conn.send(message)

    def init_call(self, recipient: str):
        """Send a call notification to the recipient via the server

    Args:
        recipient (str): the user that want to be called
    """

    def call(self, recipient: str):
        """initiate call

    Args:
        recipient (str): the user that the user calling to
    """

    def end_call(self, recipient: str):
        """end the call to the recipient

    Args:
        recipient (str): _description_
    """

    def end_connection(self):
        """
    End the connection
    """
