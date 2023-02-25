import requests as req

def get_pokemon(id):
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    res = req.get(url)

    if res.status_code not in range(200, 300):
        print("Everything is AAAAAAAAAAAAAAAAAH 🔥🔥🔥")
        return {"error": True}

    data_json = res.json()

    pokemon = {
        "name": data_json["name"],
        "number": data_json["id"],
        "hp": data_json["stats"][0]["base_stat"],
        "attack": data_json["stats"][1]["base_stat"],
        "defense": data_json["stats"][2]["base_stat"],
        "special_attack": data_json["stats"][3]["base_stat"],
        "special_defense": data_json["stats"][4]["base_stat"],
        "speed": data_json["stats"][5]["base_stat"],
        "type_of_poke": data_json["types"][0]["type"]["name"],
        "height": data_json["height"],
        "weight": data_json["weight"],
        "image": data_json["sprites"]["front_default"]
    }

    return pokemon