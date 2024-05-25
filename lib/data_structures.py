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
    names = []
    for food in spicy_foods:
        names.append(food["name"])
        return names

    pass


def get_spiciest_foods(spicy_foods):
    spiciest = []
    for food in spicy_foods :
        if food ["heat_level"] > 5:
         spiciest.append({food.copy()})
    return spiciest 


def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
      name = food["name"]
      origin = food.get("origin", "Unknown")  # Get origin with default "Unknown"
      heat_level = food["heat_level"]
      chili_peppers = "" * heat_level

      print(f"{name} ({origin}) | Heat Level: {chili_peppers}")



def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    pass

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    total_heat = 0
    num_foods = len(spicy_foods)

    if num_foods == 0:
      return None  

    for food in spicy_foods:
     total_heat += food["heat_level"]

    return total_heat / num_foods

def create_spicy_food(spicy_foods, spicy_food):
    new_list = spicy_foods.copy()
    new_list.append(spicy_food)
    return new_list 
