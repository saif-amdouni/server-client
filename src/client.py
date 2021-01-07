import socket
import threading
from time import sleep

class client(socket.socket):
    def __init__(self,family,kind,name):
        socket.socket.__init__(self,family,kind)
        self.name = name
    def send_msg(self,data):
        data=data.encode("utf8")
        self.sendall(data)
        #print(client.recv(2048).decode("utf8"))
    def get_msg(self):
        data = str(input())
        return(data)

def synch_name(client):
    name = str(input("what's your name ! : "))
    client.send_msg(name)
    client.name = name
    print(f"[Name sent] : {name}")
def get_msg_server():
    while(True):
        print(client.recv(2048).decode("utf8"))
    
#get server ip!
server = str(input("server  :"))
port = int(input("port  :"))
client = client(socket.AF_INET,socket.SOCK_STREAM,"")
com=False
'''programme principal'''
try : 
    client.connect((server,port))
    print("client connected !")
    print("-----------------------------------------------------------")
    synch_name(client)
    get_msg_thread=threading.Thread(target=get_msg_server)
    get_msg_thread.start()
    com=True
    
except Exception as e :
    print("can't connect to server !")
    client.close()
if(com):
    try:
        while(True):
                msg = client.get_msg()
                client.send_msg(msg)
                if(msg == "!Disconnect"):
                    break
    except Exception as e :
        print("connexion lost !")
    finally :
        client.close()