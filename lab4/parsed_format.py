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
    output = net_connect.send_command("show ip route", use_textfsm=True)
    net_connect.disconnect()
    print(type(output))
    for route in output:
        print(route["protocol"],route["network"],route["distance"],route["metric"] )
        #print(route["network"])
        #print(route["distance"])
        #print(route["metric"])#
     # Print the first dictionary to see the available keys
    #if output:
        #print(output[0])
    
    # Iterate through the output and print the available keys
    #for route in output:
        #print(route.keys())