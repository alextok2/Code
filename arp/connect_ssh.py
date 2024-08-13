import getpass
from netmiko import ConnectHandler
from paramiko import SSHClient, AutoAddPolicy
import json
import datetime

# host = "jump.mmk.ru"
host = "10.8.175.1"
port = 22
username = "tokarev200557"
password = getpass.getpass() 
filename = "C:\\Users\\alext\\code\\arp\\config.txt"

def connect_to_device(host, username, password, port, device_type='cisco_ios', channel=None):
    device = {
    'device_type': device_type,
    'host': host,
    'username': username,
    'password': password,
    'secret': 'enablepass',
    'port': port,
    }
    
    connection = ConnectHandler(**device)
    return connection


net_connect = connect_to_device(host, username, password, port)
# net_connect.enable()


with open(filename) as file:
    commands = [line.rstrip() for line in file]



outputs = []
results = {}


for line in commands:
    output = net_connect.send_command(line)
    outputs.append(output)


for command, output in zip(commands, outputs):
    # formatted_output = "\\n" + "\\n".join(line.strip() for line in output.split("\\n"))
    results[command] = output

with open("device_output.txt", "w") as txt_file:
    for command, output in zip(commands, outputs):
        # Get the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Write the command, timestamp, and output to the file
        txt_file.write(f"Command: {command}\n")
        txt_file.write(f"Executed at: {timestamp}\n")
        txt_file.write("Output:\n")
        txt_file.write(output)
        txt_file.write("\n" + "-"*40 + "\n\n")


net_connect.disconnect()

