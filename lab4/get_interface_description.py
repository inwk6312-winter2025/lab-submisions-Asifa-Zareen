from netmiko import ConnectHandler
r1 = {"device_type": "cisco_ios",
        "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": "22"}
r2 = {"device_type": "cisco_ios",
    "ip": "192.168.1.102",
    "username": "student",
    "password": "Meilab123",
    "port": "22"}
r3 = {"device_type": "cisco_ios",
    "ip": "192.168.1.103",
    "username": "student",
    "password": "Meilab123",
    "port": "22"}

show_commands = [
    "show interface description",
    "show ip interface brief",
    "show version",
    "show running-config"
]

for device in (r1, r2, r3):
    net_connect = ConnectHandler(**device)
    for command in show_commands:
        output = net_connect.send_command(command)
        print("-"*100)
        print(f"Command: {command}")
        print(output)
        print("-"*100)
    net_connect.disconnect()