import socket

class Client:
   def __init__(self):
        self.server_ip = "127.0.0.1"
        self.server_port = 7700
        self.socket_make(self.server_ip, self.server_port)

   def socket_make(self, ip, port):
       self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       self.s.connect((ip, port))
       text = input("tell me anything: ")
       self.s.send(text.encode("utf-8"))

       data = self.s.recv(1024)
       print(data.decode("utf-8"))

client = Client()