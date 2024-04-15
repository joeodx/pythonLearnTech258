import json
#
# # Converting json to python
#
# with open("new_json_file.json") as jsonfile:
#     car = json.load(jsonfile)
#     print(type(car))
#     print(car["name"])
#     print(car["engine"])

# Loads example
path_to_json = "example.json"
json = json.loads(open(path_to_json).read())
value = json["name"]

print(value)

# json. load takes a file
# json. loads takes a string

