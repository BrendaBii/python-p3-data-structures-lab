spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    my_list = [n.get('name') for n in spicy_foods]
    return my_list

def get_spiciest_foods(spicy_foods):
    my_dict = [item for item in spicy_foods if int(item["heat_level"]) > 5]
    return my_dict

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        heat = '🌶' * int(item['heat_level'])
        print(f"{item['name']} ({item['cuisine']}) | Heat Level: {heat}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        if int(item['heat_level']) > 5:
          heat = '🌶' * int(item['heat_level'])
          print(f"{item['name']} ({item['cuisine']}) | Heat Level: {heat}")

def get_average_heat_level(spicy_foods):
    my_list = [n['heat_level'] for n in spicy_foods]
    average =sum(my_list) / len(my_list)
    return average

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
