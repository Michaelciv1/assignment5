"""
Michael Wallerius 
Assignment 5 
3/17/2021
server.py
"""

import socket 
import sys
import os
import threading 

def main():
    HOST = "localhost"
    PORT_LIST = [5552,5553,5554,5555]
    if len(sys.argv) > 2 or int(sys.argv[1]) >= 5:
        print("invalid command line input")
        quit()
    ClientCount = int(sys.argv[1])
    threads = []

    for port in range(ClientCount):
        s = socket.socket()
        try:
            s.bind((HOST, PORT_LIST[port]))
        except socket.error as e:
            print(str(e))

        print('Waiting for a connection at',str(PORT_LIST[port]))
        s.listen()

        t = threading.Thread(target = threaded_client, args = (s, ))
        threads.append(t)
        t.start()

def threaded_client(s):
    """Creates a thread for each client that the user specifies in the command line argument"""
    try: 
        s.settimeout(15)
        (client, addr) = s.accept()
    except socket.timeout:
        print("timed out")
        return
    mesg = os.getcwd()
    print('sending',mesg)
    client.send(mesg.encode('utf-8'))
    while True:
        currentDirectory = os.getcwd()
        fromClient = client.recv(1024).decode('utf-8')

        if not fromClient:
            break

        if fromClient[0] == "l":
            currentDirectory = os.getcwd()
            mesg = "Directories and files found under "+ currentDirectory +"\n"
            directoryList = os.listdir()
            if not directoryList:
                client.send("This directory is empty\n".encode('utf-8'))
            else:
                for item in directoryList:
                    mesg += item + '\n'
                client.send(str(mesg).encode('utf-8'))
        
        elif fromClient[0] == "c":
            try: 
                os.chdir(currentDirectory+"/"+fromClient[1:])
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

    client.close()
    s.close()

            
if __name__ == "__main__":
    main()
        
        
