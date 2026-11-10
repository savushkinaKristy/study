import requests

# получаем первых 20 покемонов
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=20")
dictionary = response.json()
# получаем имена покемонов
names = []
for pokemon in dictionary["results"]:
    names.append(pokemon["name"])
print(names)

# получаем имя одного из покемонов
one_name = input("Введите имя одного из покемонов: ")
response_pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{one_name}")

if response_pokemon.status_code == 200:
    inf_pokemon = response_pokemon.json()
    print(inf_pokemon["name"])
    for tip in inf_pokemon["types"]:
        print(tip["type"]["name"])
    print(inf_pokemon["weight"])
    print(inf_pokemon["height"])
    for ability in inf_pokemon["abilities"]:
        print(ability["ability"]["name"])
else:
    print("Покемон не найден")

