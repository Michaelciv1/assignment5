import socket
import sys

HOST = '127.0.0.1'
PORT = int(sys.argv[1])

def main():
    with socket.socket() as s:
        s.connect((HOST,PORT))
        print("Client connected to:",HOST,"port:",PORT)
        directoryName = s.recv(1024).decode('utf-8')
        print("Received from server:", directoryName)

        while True:
            print("\nc: change directory\nl: list directory\nf: create file\nq: quit")

            userRequest(s)

def userRequest(s):
    while True:
        mesg = input("Enter choice: ")
        if mesg == 'l':
            listDirectory(s, mesg)
            # s.send(mesg.encode('utf-8'))
            break
        elif mesg == "c":
            changeDirectory(s, mesg)
            break
        elif mesg == 'f':
            createNewFile(s, mesg)
            break
        elif mesg == 'q':
            quit()
        else:
            print ("Invalid selection, please try again.")

def changeDirectory(s, mesg):
    # while True: 
    newPath = input("Enter path, starting from current directory: ")
    newMesg = mesg+newPath
    s.send(newMesg.encode('utf-8'))

    fromServer = s.recv(1024).decode('utf-8')
    print(fromServer)
    return

def listDirectory(s, mesg):
    s.send(mesg.encode('utf-8'))
    fromServer = s.recv(1024).decode('utf-8')
    print(fromServer)
    return

def createNewFile(s, mesg):
    newFile = input("Enter filename: ")
    newMesg = mesg+newFile
    s.send(newMesg.encode('utf-8'))
    fromServer = s.recv(1024).decode('utf-8')
    print(fromServer)
    return
    

    
            
if __name__ == "__main__":
    main()