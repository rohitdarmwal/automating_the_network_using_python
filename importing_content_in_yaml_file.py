import yaml
from pprint import pprint

my_dict = {
    'rtr10': {'bgp_peers': ['10.1.1.1', '10.100.1.2', '10.23.1.2', '12.3.4.2'],
            'device_type': 'juniper_junos',
            'ip_addr': '10.1.1.1',
            'password': 'whatever',
            'username': 'admin'}
}
with open("my_devices.yml","w") as f:
    output = yaml.dump(my_dict, f)

pprint(output)
