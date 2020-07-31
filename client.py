import socket, threading, sys

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(("0.0.0.0", 12345))
        self.sock.listen(1)
		
    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                break
	
    def run(self):
        while True:
            c,a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c,a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print (self.connections)
			
class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def sendmsg(self):
        while True:
            self.sock.send(input("", "utf-8"))
		
    def __init__(self, address):
        self.sock.connect((address, 12345))
		
        iThread = threading.Thread(target=self.sendmsg)
        iThread.daemon = True
        iThread.start()
		
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print (data)
				
if len(sys.argv) > 1:
	client = Client(sys.argv[1])
else:
	server = Server()
	server.run()