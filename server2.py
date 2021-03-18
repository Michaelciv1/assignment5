import socket 
import sys
import os
import threading 

def main():
    HOST = "localhost"
    PORT_LIST = [5552,5553,5554,5555]
    ClientCount = int(sys.argv[1])
    threads = []

    for port in range(ClientCount):
        s = socket.socket()
        try:
            s.bind((HOST, PORT_LIST[port]))
            print(HOST,PORT_LIST[port])
        except socket.error as e:
            print(str(e))

        print('Waiting for a connection at',str(PORT_LIST[port]))
        s.listen()

        t = threading.Thread(target = threaded_client, args = (s, ))
        threads.append(t)
        t.start()

def threaded_client(s):
    try: 
        s.settimeout(15)
        (client, addr) = s.accept()
    except socket.timeout:
        print("timed out")
        return
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))
    mesg = os.getcwd()
    client.send(mesg.encode('utf-8'))
    while True:
        currentDirectory = os.getcwd()
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
                for file_folder in directoryList:
                    mesg += file_folder + "\n"
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
    client.close()
    s.close()

            
if __name__ == "__main__":
    main()
        
        
