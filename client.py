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
            print("\nc: change directory\nl: list directory\nc: create file\nq: quit")

            userRequest(s)
            fromServer = s.recv(1024).decode('utf-8')
            print(fromServer)

def userRequest(s):
    while True:
        mesg = input("Enter message to send: ")
        if mesg == 'l':
            s.send(mesg.encode('utf-8'))
            break
        elif mesg == "c":
            s.send(mesg.encode('utf-8'))
            break
        elif mesg == 'n':
            s.send(mesg.encode('utf-8'))
            break
        elif mesg == 'q':
            quit()
        else:
            print ("Invalid selection, please try again.")

def changeDirectory():
    return

def listDirectory():
    return

def createNewFile():
    return
    

    
            
if __name__ == "__main__":
    main()