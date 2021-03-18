import socket 
import sys
import os

HOST = "localhost"
PORT = 5552

print (sys.argv[0])

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

        if not fromClient:
            break
        print("This is",type(fromClient))

        if fromClient[0] == "l":
            mesg = "Directories and files found under "+ currentDirectory +"\n"
            directoryList = os.listdir()
            if not directoryList:
                conn.send("This directory is empty".encode('utf-8'))
            else:
                for file_folder in directoryList:
                    mesg += file_folder + "\n"
                conn.send(str(mesg).encode('utf-8'))
        
        elif fromClient[0] == "c":
            try: 
                os.chdir(currentDirectory+fromClient[1:])
                currentDirectory = os.getcwd()
                returnMessage = "Directory as been changed to " + currentDirectory
                conn.send(returnMessage.encode('utf-8'))
            except FileNotFoundError:
                error = fromClient[1:] + " does not correspond to an existing directory"
                conn.send(error.encode('utf-8'))

        

            
        
        
