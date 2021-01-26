from netmiko import Netmiko
from getpass import getpass
ssh_pass = getpass()
enable_pass = getpass()
ip_addr = open("ip_addr.txt")
for u in ip_addr:
    l = u.strip()
    device = {'host': l,'username': 'roshan', 'password': ssh_pass, 'secret': enable_pass, 'device_type': 'cisco_ios'}
    net_conn = Netmiko(**device)
    print("----------------------------------entering in device-------------")
    print(net_conn.find_prompt())
    output = net_conn.send_config_from_file("config.txt")
    print(output)
    print(net_conn.send_command_timing("sh ip int br"))

