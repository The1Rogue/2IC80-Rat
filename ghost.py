import time
import os

services = {services}
isRoot = os.popen("echo $USER").read()=="root\n"

while True:
	time.sleep({sleepTime})
	for i in services:
		if os.popen("ps -ef | grep -v grep | grep {service} | wc -l".format(service=i)).read()=="0\n":
			if isRoot:
				os.system("systemctl start " + i)
			else:
				os.system("systemctl --user start " + i)

