import socket 
import sys
import os
from _thread import *

HOST = "localhost"
PORT = 5552

print (sys.argv[0])

with socket.socket() as s:
    s.bind((HOST, PORT))
    print("Server hostname:", HOST, "port:", PORT)
    s.listen()
    (client, addr) = s.accept()
    mesg = os.getcwd()
    client.send(mesg.encode('utf-8'))
    currentDirectory = os.getcwd()
    
    while True:
        fromClient = client.recv(1024).decode('utf-8')

        if not fromClient:
            break
        print("This is",fromClient)

        if fromClient[0] == "l":
            mesg = "Directories and files found under "+ currentDirectory +"\n"
            directoryList = os.listdir()
            if not directoryList:
                client.send("This directory is empty".encode('utf-8'))
            else:
                for item in directoryList:
                    mesg += item + "\n"
                client.send(str(mesg).encode('utf-8'))
        
        elif fromClient[0] == "c":
            try: 
                os.chdir(currentDirectory+fromClient[1:])
                currentDirectory = os.getcwd()
                returnMessage = "Directory as been changed to " + currentDirectory
                client.send(returnMessage.encode('utf-8'))
            except FileNotFoundError:
                error = fromClient[1:] + " does not correspond to an existing directory"
                client.send(error.encode('utf-8'))
            
        elif fromClient[0] == "f":
            filename = fromClient[1:]
            if os.path.exists(filename):
                client.send("File already exists".encode('utf-8'))
            else: 
                with open(filename, 'w') as fp: 
                    pass
                returnMessage = "File created at " + currentDirectory
                client.send(returnMessage.encode('utf-8'))
            

        

            
        
        
