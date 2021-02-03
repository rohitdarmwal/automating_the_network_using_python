import jinja2
template = """
{%- for i in vlan_id%}
vlan {{i}}
    name {{vlan_name}}{{i}}
{%- endfor %}"""
vlan_data = {"vlan_id": ["501","502","503","504","504","505","506","507","508"],
             "vlan_name": "blue"}
template1 = jinja2.Template(template)
print(template1.render(vlan_data))
