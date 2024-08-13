import getpass
from netmiko import ConnectHandler
import connect_serial

device = {
    'device_type': 'cisco_ios_serial',
    'ip': '192.168.0.1',
    'username': 'admin',
    'password': '',
    'secret': 'secret',
    'serial_settings': {
            "port": "COM5",
            "baudrate": 9600,
            "bytesize": connect_serial.EIGHTBITS,
            "parity": connect_serial.PARITY_NONE,
            "stopbits": connect_serial.STOPBITS_ONE,
        }
}

net_connect = ConnectHandler(**device)
net_connect.enable()

# output = net_connect.send_command('show ip int brief')
# output = net_connect.send_config_set(line)

filename = "C:\\Users\\alext\\code\\arp\\config.txt"

with open(filename) as file:
    lines = [line.rstrip() for line in file]
print(lines)

for line in lines:
    output = net_connect.send_command(line)

    print(output)   

net_connect.disconnect()

