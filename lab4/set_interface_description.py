from netmiko import Netmiko
devices = [{"device_type": "cisco_ios",
            "ip": "192.168.1.101",
            "username": "student",
            "password": "Meilab123",
            "port": "22",}]
#description = 'Description set with Netmiko'
#description_config = ["interface GigabitEthernet3",
                       # f"description {description}"]
loopback_interface = 'Loopback0'
loopback_ip = '150.1.1.1'
loopback_mask = '255.255.255.255'

loopback_config = [
    f"interface {loopback_interface}",
    f"ip address {loopback_ip} {loopback_mask}",
    "no shutdown"
]

for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_config_set(loopback_config)
    print(output)
    net_connect.disconnect()

#for device in devices:
    #net_connect = Netmiko(**device)
    #output = net_connect.send_config_set(description_config)
    #print(output)
    #net_connect.disconnect()