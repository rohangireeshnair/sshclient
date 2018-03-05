import paramiko
import getpass

def sshconnect(username, passwd, hostname, port):
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.load_system_host_keys()
    ssh_client.connect(hostname, port, username, passwd)
    return ssh_client
