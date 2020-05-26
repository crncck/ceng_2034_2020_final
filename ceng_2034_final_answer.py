#Ayşe Ceren Çiçek - 170709009

#! /usr/bin/python3
import os
import requests
import re
import uuid
from urllib.parse import urlparse

#create a child process and print its pid
def childParent():
	n = os.fork()
	if(n > 0):
		print("PID of the parent process: {}" .format(os.getpid()))
	else:
		print("PID of the child process: {}".format(os.getpid()))

childParent()

#download the files via given URL list
urls = ['http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg',
'https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png',
'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg',
'http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg',
'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg']

def download_file(url, file_name):
	r = requests.get(url, allow_redirects=True)
	file = file_name if file_name else str(uuid.uuid4())
	open(file, "wb").write(r.content)

for u in urls:
	filename = urlparse(u)
	download_file(u, os.path.basename(filename.path))










