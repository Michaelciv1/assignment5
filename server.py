import socket 
import sys
import os

HOST = "localhost"
PORT = 5552

print (sys.argv)

with socket.socket() as s:
    s.bind((HOST, PORT))
    print("Server hostname:", HOST, "port:", PORT)
    s.listen()
    (conn, addr) = s.accept()
    mesg = os.getcwd()
    conn.send(mesg.encode('utf-8'))
    currentDirectory = os.getcwd()
    
    while True:
        fromClient = conn.recv(1024).decode('utf-8')

        if fromClient == "l":
            mesg = "Directories and files found under "+ currentDirectory +"\n"
            directoryList = os.listdir()
            for file_folder in directoryList:
                mesg += file_folder + "\n"
            conn.send(str(mesg).encode('utf-8'))
        
        elif fromClient == "n":
            