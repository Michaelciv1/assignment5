"""
Michael Wallerius 
Assignment 5 
3/17/2021
client.py
"""

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
            print("c: change directory\nl: list directory\nf: create file\nq: quit")

            userRequest(s)

def userRequest(s):
    """Prompts, reads in, and validates the user's choice of the 4 possible requests. Continues re-prompting until you get a valid choice.""" 
    while True:
        mesg = input("Enter choice: ")
        if mesg == 'l':
            listDirectory(s, mesg)
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
    """changes directory on the server side"""
    newPath = input("Enter path, starting from current directory: ")
    newMesg = mesg+newPath
    s.send(newMesg.encode('utf-8'))

    fromServer = s.recv(1024).decode('utf-8')
    print(fromServer,'\n')
    return

def listDirectory(s, mesg):
    """lists the current working directory on the server side"""
    s.send(mesg.encode('utf-8'))
    fromServer = s.recv(1024).decode('utf-8')
    print(fromServer)
    return

def createNewFile(s, mesg):
    """creates a new file in the current working directory, checks if the file already exists and prints an error"""
    newFile = input("Enter filename: ")
    newMesg = mesg+newFile
    s.send(newMesg.encode('utf-8'))
    fromServer = s.recv(1024).decode('utf-8')
    print(fromServer,'\n')
    return
    

    
            
if __name__ == "__main__":
    main()