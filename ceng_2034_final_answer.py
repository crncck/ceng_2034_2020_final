#Ayşe Ceren Çiçek - 170709009

#! /usr/bin/python3
import os
import requests
import sys
import re
import uuid
import os.path
from os import path
import urllib.parse
from urllib.parse import urlparse
import hashlib
import threading

#create a child process and print its pid
pid = os.fork()
if(pid > 0):
	print("PID of the parent process: {}" .format(os.getpid()))
else:
	print("PID of the child process: {}".format(os.getpid()))


print("\n")


#download the files via given URL list with child process
urls = ['http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg',
'https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png',
'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg',
'http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg',
'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg']

def download_file(url, file_name):
	r = requests.get(url, allow_redirects=True)
	a = path.exists(file_name)
	if a == 0:
		file = file_name if file_name else str(uuid.uuid4())
		
	else:
		file_name = file_name.split('.')[0]+'(2).'+file_name.split('.')[1]
		file = file_name
		
	open(file, "wb").write(r.content)

def childProcess(pid):

	children = []

	if pid > 0:
		children.append(pid)
	else:
		#the child process will download the files
		for u in urls:
			filename = urlparse(u)
			download_file(u, os.path.basename(filename.path))
		os._exit(0)

	#to avoid orphan processes 
	for i, proc in enumerate(children):
		os.waitpid(proc, 0)
	print("Parent process is closing")

childProcess(pid)


#control the duplicates in the folder
def findFiles(current_directory):
	listFiles = os.listdir(current_directory)
	allFiles = []
	
	for i in listFiles:
		fullpath = os.path.join(current_directory, i)
		allFiles.append(fullpath)
	
	return allFiles


def file_as_bytes(fname):
	hash_md5 = hashlib.md5()
	with open(fname,"rb") as f:
		for chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(chunk)
	return hash_md5.hexdigest()

def checkDuplicates(array):
	for i in array:
		if array.count(i) > 1:
			index = findDuplicates(array)
			return index

	return False

def findDuplicates(array):
	size = len(array)
	duplicates = []
	index = []
	for i in range(size):
		k = i + 1
		for j in range(k, size):
			if array[i] == array[j] and array[i] not in duplicates:
				duplicates.append(array[i])
				index.append(i)
	return index


current_directory = (os.path.abspath(os.getcwd()))
hexdig = []
files = findFiles(current_directory)

for i in files:
	a = file_as_bytes(i)
	hexdig.append(a)
	print(a)

print("\n")

duplicate = checkDuplicates(hexdig)
if duplicate == 0:
	print("No duplicate in the folder.")
else:
	print("The duplicate files:")
	for i in duplicate:
		file_Name = files[i]
		head_tail = os.path.split(file_Name)
		print(head_tail[1])





