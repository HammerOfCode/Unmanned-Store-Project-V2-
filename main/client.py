from email import message
from http import client
import socket

HEADER = 64
PORT = 5050 
SERVER = "172.30.69.==="
FORMAT = 'utf-8'
DISCONNECT_MESSAGE= "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR= (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
# listmsg=[1,2,3,4]
# listmsg = str(listmsg)
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
# send(listmsg)

#send(DISCONNECT_MESSAGE)


