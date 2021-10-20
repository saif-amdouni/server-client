import socket
import threading
class server(socket.socket):
    def __init__(self,family,kind):
        socket.socket.__init__(self,family,kind)
        self.clients = {}
        self.names = {}
    

def handle_client(conn,address):
    print(f"New client [{address}]")
    while (True):
        try :
            data= conn.recv(1024)
            data= data.decode("utf8")
            print(f"{server.names[address]} : {data}")
            for key in server.clients.keys() :
                if (key!=address):
                    server.clients[key].send((f"{server.names[address]} : {data}").encode("utf8"))
            
                    
            if (data == "!Disconnect"):
                conn.close()
                print(f"client at [{address}] has disconnected!")
                server.clients.pop(address)
                break
            
        except Exception as e :
            server.clients.pop(address)
            print(f"conexion with [{address}] is lost!")
            break
def start_server(server):
    server.listen()
    while True:
        conn,addr = server.accept()
        name= conn.recv(1024).decode("utf8")
        server.clients[addr]=conn
        server.names[addr]=str(name)
        conn.send("name received !".encode("utf8"))
        thread = threading.Thread(target=handle_client , args=(conn,addr))
        thread.start()
        print(f"active connections = {threading.activeCount()-1}")
        print(f"Clients = {server.clients.keys()}")


if __name__ == "__main__":
    host , port =('',5566)
    server = server(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((host,port))
    print("le serveur est demarré")
    start_server(server)
