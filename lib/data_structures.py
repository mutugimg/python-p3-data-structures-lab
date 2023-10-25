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
    result = [food["name"] for food in spicy_foods]
    # print(result)
    return result
get_names(spicy_foods)
    

def get_spiciest_foods(spicy_foods):
    heat_level = [ item for item in spicy_foods if item ["heat_level"] > 5]
    # print(heat_level)
    return heat_level
get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for spice in spicy_foods:
        print(f"{spice['name']} ({spice['cuisine']}) | Heat Level: {'🌶' * spice['heat_level']}")
    return spice
# print_spicy_foods(spicy_foods)
pass


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine == food["cuisine"]:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = [
        food for food in spicy_foods if food.get("heat_level") > 5]
    print_spicy_foods(spiciest_foods)

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    heat_level_sum = sum([food["heat_level"] for food in spicy_foods])
    heat_level_foods= len(spicy_foods)
    avrg_heat_level = int(heat_level_sum/heat_level_foods)
    print(avrg_heat_level)
    return avrg_heat_level
   
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.extend([spicy_food])
    return spicy_foods

spicy_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

new_spicy_foods = create_spicy_food(spicy_foods, spicy_food)
print(new_spicy_foods[3])
