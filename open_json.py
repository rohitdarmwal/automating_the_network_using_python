from pprint import pprint
import json

filename = "my_file.json"
with open(filename) as f:
    json_data = json.load(f)
pprint(json_data)
num_1 = input("enterno.")
print(num_1)