import os
import getpass

os.system("tput setaf 4")
print("\t\t\t Welcome to my Menu!!")
os.system("tput setaf 11")
print("\t\t\t---------------------")


pwd=getpass.getpass("Enter password:")

if pwd!= "VD":
	print("Password Invalid!!")
	exit()

r=input("Where you want to run this menu?(local/remote):")
print(r)

while True:
	os.system("clear")
	print("""
	\n 
	PRESS 1: To reboot the system
	PRESS 2:To configure webserver
	PRESS 3:To launch docker container
	PRESS 4:To remove docker image
	PRESS 5:To create partitions
	PRESS 6:To configure Hadoop Namenode
	PRESS 7:To configure Hadoop Datanode
	PRESS 8:To configure Ansible on Controller Node
	PRESS 9:To exit
	""")
	
	ch=int(input("Enter your choice :"))
	print(ch)

	if r == "local":
		if ch == 1:
			os.system("reboot")
		elif ch ==2:
			os.system("yum install httpd")
			os.system("cd /var/www/html")
			f1=input("Enter file you want to create with its path:")
			os.system("touch {}".format(f1))
			os.system("systemctl start httpd")
			os.system("systemctl status httpd")
			
		elif ch ==3:
			os.system("yum install docker-ce")
			OS=input("Enter the name of container image to want to install:")
			os.system("docker pull {}".format(OS))
			os.system("docker run -it {}".format(OS))
		elif ch ==4:
			image=input("Enter the name of the image and its version:")
			os.system("docker rmi {}".format(image))
		elif ch ==5:
			os.system("fdisk -l")
			hd_name=input("Enter your disk name:")
			os.system("fdisk {}".format(hd_name))
			os.system("fdisk -l")
			pt_name=input("Enter name of partition:")
			os.system("mkfs.ext4 {}".format(pt_name))
			path=input("Enter folder path on which you want to mount partition:")
			os.system("mkdir {}".format(path))
			os.system("mount {} {}".format(pt_name,path))
			print("Disk Mounted ready to go!!...")	
		elif ch ==6:
			print("------MASTER NODE-------")
			print("...Setup configuration files...")
			os.system("vim /etc/hadoop/hdfs-site.xml")
			os.system("vim /etc/hadoop/core-site.xml")
			os.system("hadoop namenode -format")
			os.system("hadoop-daemon.sh start namenode ")
			os.system("jps")
		elif ch ==7:
			print("------SLAVE NODE-------")
			print("...Setup configuration files...")
			os.system(" gedit /etc/hadoop/hdfs-site.xml")
			os.system(" gedit /etc/hadoop/core-site.xml")
			os.system(" hadoop-daemon.sh start datanode ")
			os.system(" jps")		
		elif ch ==8:
			os.system("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
			os.system("yum install sshpass")
			os.system("pip3 install ansible")
			os.system("ansible --version")
			print("----Setting up Configuration file----")
			os.system("mkdir /etc/ansible")
			os.system("vim /etc/ansible/ansible.cfg")
			inv_name=input("Enter the file or inventory path:")
			os.system("vim {}".format(inv_name))
			os.system("ansible all --list-hosts")
			print("!! Controller Node has been setup!!...")					
		elif ch ==9:
			exit()
		else:
			print("Not supported")
	elif r == "remote":
		ip=input("Enter remote IP:")
		
		if ch == 1:
			os.system("ssh {} reboot".format(ip))
		elif ch ==2:			
			os.system("ssh {} yum install httpd ".format(ip))
			os.system("ssh {} cd /var/www/html".format(ip))
			f1=input("Enter file you want to create with its path:")
			os.system("ssh {} touch {}".format(ip,f1))
			os.system("ssh {} systemctl start httpd ".format(ip))
			os.system("ssh {} systemctl status httpd ".format(ip))
		elif ch ==3:
			os.system("ssh {} yum install docker-ce --nobest".format(ip))
			OS=input("Enter the name of container image to want to install:")
			os.system("ssh {} docker pull {}".format(ip,OS))
			os.system("ssh {} docker run -it {}".format(ip,OS))
		elif ch ==4:
			image=input("Enter the name of the image and its version:")
			os.system("ssh {} docker rmi {}".format(ip,image))
		elif ch ==5:
			os.system("ssh {} fdisk -l")
			hd_name=input("Enter your disk name:")
			os.system("ssh {} fdisk {}".format(ip,hd_name))
			os.system("ssh {} fdisk -l")
			pt_name=input("Enter name of partition:")
			os.system("ssh {} mkfs.ext4 {}".format(ip,pt_name))
		elif ch ==6:
			print("------MASTER NODE-------")
			print("...Setup configuration files...")
			os.system("ssh -l root -X {} gedit /etc/hadoop/hdfs-site.xml".format(ip))
			os.system("ssh -l root-X {} gedit /etc/hadoop/core-site.xml".format(ip))
			os.system("ssh {} hadoop namenode -format".format(ip))
			os.system("ssh {} hadoop-daemon.sh start namenode ".format(ip))
			os.system("ssh {} jps".format(ip))
		elif ch ==7:
			print("------SLAVE NODE-------")
			print("...Setup configuration files...")
			os.system("ssh -l root -X {} gedit /etc/hadoop/hdfs-site.xml".format(ip))
			os.system("ssh -l root -X {} gedit /etc/hadoop/core-site.xml".format(ip))
			os.system("ssh {} hadoop-daemon.sh start datanode ".format(ip))
			os.system("ssh {} jps".format(ip))
		elif ch ==8:
			os.system("ssh {} dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm".format(ip))
			os.system("ssh {} yum install sshpass".format(ip))
			os.system("ssh {} pip3 install ansible".format(ip))
			os.system("ssh {} ansible --version".format(ip))
			print("----Setting up Configuration file----")
			os.system("ssh {} mkdir /etc/ansible".format(ip))
			os.system("ssh -l root -X {} gedit /etc/ansible/ansible.cfg".format(ip))
			inv_name=input("Enter the file or inventory path:")
			os.system("ssh -l root -X {} gedit {}".format(ip,inv_name))
			os.system("ssh {} ansible all --list-hosts".format(ip))
			print("!! Controller Node has been setup!!...")	
		elif ch ==9:
			exit()
		else:
			print("Not supported")
	else:
		print("Invalid Login!!")
	input("\n Press any key to continue...")
