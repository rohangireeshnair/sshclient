import paramiko
import getpass
import sys
def sshconnect(username, passwd, hostname, port):
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.load_system_host_keys()
    try :
        ssh_client.connect(hostname, port, username, passwd)
    except paramiko.ssh_exception.AuthenticationException :
        print('Authentication failure occured. Please check the following \n'
              '1. Username/Password. \n'
              '2. If ssh daemon is running on the target PC. \n')
        sys.exit(0)
    return ssh_client
