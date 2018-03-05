import paramiko
import getpass

def runcom(sshclient, cmd):
    stdin, stdout, stderr= sshclient.exec_command(cmd)
    while True :
        tbp = stdout.readline()
        if(tbp) :
            print(tbp)
        else:
            break
