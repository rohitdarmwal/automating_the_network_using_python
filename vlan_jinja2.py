# import jinja2
# vlan_name = {"vlan_id": 440,
#              "vlan_name": "management",}
# vlan_template = """ vlan {{vlan_id}}
#                          name {{vlan_name}}
#                          """
# template = jinja2.Template(vlan_template)
# print(template.render(vlan_name))

from practice_jinja2.bgp_jinja2 import Template

name = input("Enter your name: ")

tm = Template("Hello {{ name }}")
msg = tm.render(name=name)

print(msg)