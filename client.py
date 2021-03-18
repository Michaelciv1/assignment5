import socket

HOST = '127.0.0.1'
PORT = 5552

def main():
    with socket.socket() as s:
        s.connect((HOST,PORT))
        print("Client connected to:",HOST,"port:",PORT)
        directoryName = s.recv(1024).decode('utf-8')
        print("Received from server:", directoryName)

        while True:
            print("\nc: change directory\nl: list directory\nn: create file\nq: quit")

            userRequest(s)

def userRequest(s):
    while True:
        mesg = input("Enter message to send: ")
        if mesg == 'l':
            listDirectory(s, mesg)
            # s.send(mesg.encode('utf-8'))
            break
        elif mesg == "c":
            changeDirectory(s, mesg)
            break
        elif mesg == 'n':
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
   
    return
    

    
            
if __name__ == "__main__":
    main()