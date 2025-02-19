from netmiko import Netmiko
devices = [{"device_type": "cisco_ios",
            "ip": "192.168.1.101",
            "username": "student",
            "password": "Meilab123",
            "port": "22"},
            {"device_type": "cisco_ios",
                "ip": "192.168.1.102",
                "username": "student",
                "password": "Meilab123",
                "port": "22",
            },{"device_type": "cisco_ios",
                "ip": "192.168.1.103",
                "username": "student",
                "password": "Meilab123",
                "port": "22",
            }]
for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show version")
    net_connect.disconnect()
    result = output.find('uptime is')
    begin = int(result)
    end = begin + 38
    print(device['ip'] + " => " + output[int(begin):int(end)])
    
    # Extract the Configuration Register
    config_register_str = "Configuration register is"
    config_register_index = output.find(config_register_str)
    config_register_end_index = config_register_index + len(config_register_str) + 6  # Considering ' 0x2102' length
    config_register = output[config_register_index:config_register_end_index]
    print(f"{device['ip']} (Router) => {config_register}")