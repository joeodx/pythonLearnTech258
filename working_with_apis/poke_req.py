import requests
import json
import random

def pokemon_generator():
    id = random.randint(1,101)
    return id

poke_req = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(pokemon_generator()))
# print(poke_req.json())

poke_req2 = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(pokemon_generator()))
# print(poke_req2.json())

poke_data = json.loads(poke_req.text)
poke_data2 = json.loads(poke_req2.text)
# print(type(poke_data))

print(poke_data["name"])
print(poke_data2["name"])



