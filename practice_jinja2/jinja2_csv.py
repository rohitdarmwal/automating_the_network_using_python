import jinja2
import csv
csv_file = "bgp_variables.csv"
# with open(csv_file) as f:
#     read_csv = csv.DictReader(f)
f = open(csv_file)
read_csv = csv.DictReader(f)

for bgp_vars in read_csv:
    print(bgp_vars)
    advertised_routes = bgp_vars['advertised_routes']
    print(advertised_routes)
    advertised_routes = advertised_routes.split()
    bgp_vars['advertised_routes'] = advertised_routes

    template_file = "bgp_updates.j2"
    with open(template_file) as f:
        bgp_template = f.read()
    template = jinja2.Template(bgp_template)
    print(template.render(bgp_vars))
