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

print(f"Player one : {poke_data['name']}")
print(f"Player two : {poke_data2['name']}")



def pokemon_compare(player_one, player_two):
    print(f"This is Player 1 height: {float(player_one['height']) * 10} cm")
    print(f"This is Player 2 height: {float(player_two['height']) * 10} cm")
    if player_one["height"] > player_two["height"]:
        return "Player one has won!"
    elif player_one["height"] == player_two["height"]:
        return "Its a draw!"
    else:
        return "Player two has won!"

print(pokemon_compare(poke_data, poke_data2))

