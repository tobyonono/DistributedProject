import socket
import threading
import sys
import os
import signal
import glob
import subprocess
import shutil
from Queue import Queue
from threading import Thread


def _initialise(hostAddress,portNum):
	newSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	newSock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	newSock.bind((hostAddress,portNum))
	newSock.listen(10) 
	keepOpen = True
	numThreads = 100
	threadPool = Queue(numThreads)

	while keepOpen:
		conn,address=newSock.accept()
		print "ACCEPT 11"
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
		print "MSG recvd: \n"
		print message

		splitString = message.split(" ")
		if message[:12] == "KILL_SERVICE":
			print"Closing..."
			conn.close()
			run = False;
			break;	
		elif message[:2] == "ls":
			print "LS HERE \n"
			dir_path = os.path.dirname(os.path.realpath(__file__))
			print dir_path

			#subprocess.check_output(['ls','-l']) #all that is technically needed...
			print subprocess.check_output(['ls','-l'])

			#os.listdir(dir_path)
		elif splitString[0] == "cd":
			print "CD here"
			
			#subprocess.check_output(['cd', splitString[1]])
			#print subprocess.check_output(['ls','-l'])

			dir_path = os.path.dirname(os.path.realpath(__file__))
			print dir_path
			os.chdir(dir_path+"/" + splitString[1])
			print subprocess.check_output(['ls','-l'])
			
			
		elif splitString[0] == "delete":

			shutil.rmtree(splitString[1])
			print subprocess.check_output(['ls','-l'])
			print "delete blah blah"
			
		elif message[:5]== "write":
			print "write"
			file = open(fileContents + splitString[1], "w")
			file.write(splitString[2])
			file.close()
			
			
		elif message[:4]== "read":
			print "got into read"
			file = open(splitString[1])
			fileContents = file.read()
			print "%s" % (fileContents)
			
		elif message[:5]== "mkdir":

			print "got to make"
			if not os.path.exists(splitString[1]):
				os.makedirs(splitString[1])
			print subprocess.check_output(['ls','-l'])


if __name__ == '__main__':
	_initialise(sys.argv[1],int(sys.argv[2]))