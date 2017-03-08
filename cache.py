import socket
import threading
import sys
import os
import signal
from Queue import Queue
from threading import Thread
import subprocess
import shutil
import glob

cacheSize = 0
maxCacheSize = 10

cacheHistory = []
class cacheClass:
	cache = {}


	def addFileToCache(filePath, fileContents):
		if cacheSize <= maxCacheSize:
			cache[filePath] = fileContents
			cacheSize += 1 
			cacheHistory.append(filePath)

	def getFileFromCache(filePath):
		return cache[filePath]

	def isFileInCache(filePath):
		if filePath in cache:
			return True
		else:
			return False
		
	def delFromCache(filePath, fileContents):
		if cacheSize == maxCacheSize:
			oldestEntry = cacheHistory.pop(0)
			del cache[oldestEntry]

	def isCacheFull():
		if cacheSize == maxCacheSize:
			return True
		else:
			return False