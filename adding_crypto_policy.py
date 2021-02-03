import jinja2
crypto_variables = {
    "isakmp_on": True,
    "encryption_group": "AES",
}
crypto_policy = """
{% if isakmp_on %}
crypto isakmp policy 10
    encr {{encryption_group}}
    authentication pre-share
    group 5
crypto isakmp key my_key address 1.1.1.1 no-xauth
crypto isakmp keepalive 10 periodic
{% endif %}"""
template = jinja2.Template(crypto_policy)
print(template.render(crypto_variables))
