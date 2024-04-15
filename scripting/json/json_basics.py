import json

car_data = {
    "name": "tesla",
    "engine": "electric"
}

print(type(car_data))

# json.dumps ---> serialises json to a formatted string

car_data_json_string = json.dumps(car_data)
print(car_data_json_string)

# json.dump() --> Creates a stream object and expects a file object to write to and creates a json file
with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)
