import jinja2
advertised_routes = ['10.1.1.0/24', '10.10.2.0/24', '10.10.3.0/24']
bgp_vars = {
    "local_as": 10,
    "peer1_ip": "10.255.255.2",
    "peer1_as": 20,
    "peer1_ipv6": False,
    "advertised_routes": advertised_routes,
}
template_file = "bgp_updates.j2"
with open(template_file) as f:
    bgp_template = f.read()

template = jinja2.Template(bgp_template)
print(template.render(bgp_vars))
