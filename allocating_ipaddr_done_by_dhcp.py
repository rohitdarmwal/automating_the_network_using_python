available_ip = set()
usable_ips = set()
def  print_list():
    available_ip_list = list(available_ip)
    usable_ips_list= list(usable_ips)
    if len(available_ip_list) > len(usable_ips_list):
        for _ in range(0,len(available_ip_list) - len(usable_ips_list) ):
            usable_ips_list.append("")
    elif len(usable_ips_list) > len(available_ip_list):
        for _ in range(0,len(usable_ips_list)-len(available_ip_list)):
            available_ip_list.append("")
    print()
    print("-----------------------------available used---------------")
    print("    ----------------    --------------")
    for available_ips ,usable_ip in zip(available_ip_list,usable_ips_list):
        print(f"    {available_ips:>16}    {usable_ip:<16}")
for i in range(180,200,3):
    available_ip.add('10.1.1.'+ str(i))
print_list()
while True:
    ip_addr = input("enter the ip")
    if ip_addr in available_ip:
        print(f"-- allocating IP address: {ip_addr}")
        usable_ips.add(ip_addr)
        available_ip.remove(ip_addr)
        print_list()
    print("-------------------available_ip-------------------")
    print(available_ip)
    print("-------------------usable_ips-----------------")
    print(usable_ips)
