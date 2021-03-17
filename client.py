import socket

HOST = '127.0.0.1'
PORT = 5552

with socket.socket() as s:
    s.connect((HOST,PORT))
    print("Client connected to:",HOST,"port:",PORT)

    mesg = input("Enter message to send: ")
    s.send(mesg.encode('utf-8'))
    while mesg != 'q':
        fromServer = s.recv(1024).decode('utf-8')
        print("Received from server:", fromServer)