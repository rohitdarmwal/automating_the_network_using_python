import jinja2
bgp_vars = {
    "peer1_ip": "10.255.255.2",
    "peer1_os": 20,
}

bgp_template = '''
feature bgp 
router bgp 10
   address-family ipv4 unicast
   neighbor {{peer1_ip}} remote as {{peer1_os}}
   '''
t = jinja2.Template(bgp_template)
print(t.render(bgp_vars))