#settings if run as root
root = {"targetDir": "/etc/sysDiag/", "serviceLoc": "/etc/systemd/system/"}

#settings if run without root
user = {"targetDir": "~/.sysDiag/", "serviceLoc": "~/.config/systemd/user/"}

#name of serveral files
tarName = "systemDiagnostics.tar"
serviceName = "sys-diagnostics.service"

#service script to inject
service = "[Unit]\nDescription=\"tracks system details\"\n[Service]\nType=simple\nExecStart=/usr/bin/python3 {targetPath}"
