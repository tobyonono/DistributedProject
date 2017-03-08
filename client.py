import socket
import threading
import sys
import os
import signal
from Queue import Queue
from threading import Thread



def _initialise(hostAddress,portNum):
	global newSock
	newSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	newSock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	newSock.connect((hostAddress,portNum))
	makeServerConn()


def makeServerConn():
	isActive = True
	checkInput = True

	while isActive:
		while checkInput:
			input = raw_input()
		
			if input[:2]=="ls" or input[:2] == "cd" or input[:6] == "delete" or input[:4] == "read" or input[:5] == "write" or input[:5] == "mkdir" or input[:4] == "stop":
				print "input detected"

				newSock.send(input)
			else:
				print "Please Input valid command"
	newSock.close()

	
if __name__ == '__main__':
	_initialise(sys.argv[1],int(sys.argv[2]))








