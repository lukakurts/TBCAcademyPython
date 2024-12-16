import json


def reading_files(file_name):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError as error:
        print(error)


def finding_recipes(recipes):
    food_name = input("Please enter food you are making: ")
    food_name = food_name.title()
    if food_name in recipes:
        return recipes[food_name]["ingredients"]
    else:
        print(f"ეს კერძი არ არსებობს.")
        return []


def getting_available_recipe(recipe, markets):
    available_ingredients = {ingredient: [] for ingredient in recipe}
    for market_name, products in markets.items():
        for ingredient in recipe:
            if ingredient in products:
                available_ingredients[ingredient].append(market_name)
    return available_ingredients


def find_minimal_markets(recipe, available_ingredients):
    missing_ingredients = {ingredient for ingredient in recipe if not available_ingredients[ingredient]}
    if not missing_ingredients:
        selected_shops = set()
        for ingredient in recipe:
            best_market = available_ingredients[ingredient][0]
            selected_shops.add(best_market)
        if selected_shops:
            print(selected_shops)
    else:
        print(f"ამ კერძს ამ ქალაქში ვერ მოამზადებ")


def main():
    recipes = reading_files("Homework20/homework_1_recipes.json")
    markets = reading_files("Homework20/homework_1_markets.json")
    recipe = list(finding_recipes(recipes))
    available_ingredients = getting_available_recipe(recipe, markets)
    find_minimal_markets(recipe, available_ingredients)


if __name__ == "__main__":
    main()