from audioop import add
from concurrent.futures import thread
from http import server
import socket
from sqlite3 import connect
import threading
from tracemalloc import start

PORT = 5050 
#SERVER = "172.30.69.==="
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE= "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNCECTION] {addr} connected  ")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")

    conn.close()



def start():
    server.listen()
    print(f"[LISTENING ] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"ACTIVIE CONNECTIONS{threading.activeCount()-1}")

print("[STARTING CONNECTION] SERVER IS STARTING ")
start()