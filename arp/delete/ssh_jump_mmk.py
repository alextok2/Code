import paramiko
import getpass

def ssh_to_linux(hostname, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, port=port, username=username, password=password)
    return client

def execute_command(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.read().decode('utf-8')





password = getpass.getpass() 
linux_client = ssh_to_linux('jump.mmk.ru', 22, 'tokarev200557', password=password)
# linux_client = ssh_to_linux('github.com', 22, 'git', 'test')
telnet_command = 'lscpu'
response = execute_command(linux_client, telnet_command)
print(response)