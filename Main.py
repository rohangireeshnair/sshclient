import getpass
import paramiko
import sshconnect
import commandrunner

hostname = input('Enter the hostname:')
port = 22
username = input('Enter username:')
password = input('Enter password:')
ssh_client = sshconnect.sshconnect(username, password, hostname, port)

cmd = ''
while cmd!='exit':
    cmd=input('$')
    commandrunner.runcom(ssh_client, cmd)