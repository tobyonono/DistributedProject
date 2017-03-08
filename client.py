import socket
import threading
import sys
import os
import signal
from Queue import Queue
from threading import Thread

portNum = sys.argv[1]
IP = socket.gethostbyname(socket.gethostname())
acceptableInstructions = ["ls", "cd","delete","read","write","stop","mkdir"]

def makeServerConn():
	isActive = True
	checkInput = True
	newSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverAddress = ("localhost", portNum)
	newSock.connect(serverAddress)

	while isActive:

		while checkInput:
		input = raw_input()
		
		if input[:2]=="ls" or input[:2] == "cd" or input[:6] == "delete" or input[:4] == "read" or input[:5] == "mkdir":
			checkInput = False
		else:
			print "Please Input valid command"
		
		elif input[:4] == "stop":
			socket.write("KILL_SERVICE\n")
			isActive = False

		elif input[:5] == "write":
			splitString=input.split(" ")
			file = open(splitString[1])
			openFile = file.read()
			return openFile
	newSock.close()

	









