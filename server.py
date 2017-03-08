import socket
import threading
import sys
import os
import signal
from Queue import Queue
from threading import Thread


def _initialise(hostAddress,portNum):
	newSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	newSock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	newSock.bind((hostAddress,portNum))
	newSock.listen(10) 
	keepOpen = True
	numThreads = 10
	threadPool = Queue(numThreads)

	while keepOpen:
		try:
			conn,address=newSock.accept()
			connTuple = (conn, address)
			threadPool.put(connTuple)
			for i in range(numThreads):
                		thread = Thread(target = _dealWithClient, args = (conn,address))
                		thread.daemon = True
        	        	thread.start()

def _dealWithClient(conn, address):
	buffer = 2048
	run = True
	uniqueID = 0
	while run:
            message = conn.recv(buffer)
            splitString = message.split(" ")
         
            if message[:12] == "KILL_SERVICE":
                print"Closing..."
				conn.close()
				run = False;
				break;	
            elif splitString[0] == "ls":
                ls(conn, uniqueID, splitString)
                uniqueID += 1
            elif splitString[0] == "cd":
                cd(conn, uniqueID, splitString)
                uniqueID += 1
            elif splitString[0] == "delete":
                delete(conn, uniqueID, splitString)
                uniqueID += 1
            elif splitString[0] == "read":
                read(conn, uniqueID, splitString)
                uniqueID += 1
            elif splitString[0] == "write":
                write(conn, uniqueID, splitString)
                uniqueID += 1
            elif splitString[0] == "mkdir":
                mkdir(conn, uniqueID, splitString)
                uniqueID += 1
           


##Implement Methods

if __name__ == '__main__':
_initialise(sys.argv[1],int(sys.argv[2]))