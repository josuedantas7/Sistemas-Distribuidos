from socket import *
from constCS import *

s = socket(AF_INET, SOCK_STREAM)

s.connect((HOST, PORT))

while True:
    msg = input("Digite a mensagem: ")
    s.send(msg.encode())
    data = s.recv(1024)

s.close()