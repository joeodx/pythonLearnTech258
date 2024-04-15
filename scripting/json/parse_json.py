import json
#
# # Converting json to python
#
# with open("new_json_file.json") as jsonfile:
#     car = json.load(jsonfile)
#     print(type(car))
#     print(car["name"])
#     print(car["engine"])


path_to_json = "example.json"
json = json.load(open(path_to_json))
value = json["name"]

print(value)

