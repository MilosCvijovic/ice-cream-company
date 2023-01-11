from factory import Factory
from limit_for_ingredients import smallest_limit
import os.path
from datetime import datetime

PATH = os.getcwd()


class Warehouse:
    """Model for class Warehouse."""
    def __init__(self):
        """Initialize warehouse instance."""
        self.ingredients = {}
        self.ice_creams = {}

    def print_ingredients(self):
        """Print the quantities of all ingredients in the warehouse."""
        print("Amount of ingredients in the warehouse:")
        for ingredient, quantity in self.ingredients.items():
            print(f"{ingredient}: {quantity}")

    def print_ice_creams(self):
        """Print the quantities of all ice creams in the warehouse."""
        print("Amount of ice creams in the warehouse:")
        for ice_cream, quantity in self.ice_creams.items():
            print(f"{ice_cream}: {quantity}")

    def buy_ingredients(self, ingredient, quantity):
        """Increase the quantity of a given ingredient in the warehouse."""
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
        else:
            self.ingredients[ingredient] = quantity

    def use_ingredient(self, ingredients):
        """Decrease the quantity of given ingredients in the warehouse."""
        for ingredient in ingredients:
            if ingredient in self.ingredients:
                self.ingredients[ingredient] -= ingredients[ingredient]
            else:
                print(f"We don't have this ingredient: {ingredient}")

    def has_ingredients(self, ingredients):
        """Check if the warehouse has the specified ingredient."""
        for ingredient, quantity in ingredients.items():
            if self.ingredients.get(ingredient, 0) < quantity:
                return False
        return True

    @staticmethod
    def make_report_directory():
        """Creating directory for storing reports if it does not already exist."""
        report_path = os.path.join(PATH, "Reports")
        if not os.path.exists(report_path):
            os.mkdir(report_path)
        return report_path

    def report_for_ingredients(self):
        """Create report if the quantity of ingredients in the warehouse are below limit.
            Report is saved in Reports/Reports_to_the_head_of_the_trade and have unique number."""
        report_number = 1
        for ingredient, quantity in self.ingredients.items():
            limit = smallest_limit.get(ingredient)
            file_exists = True
            while file_exists:
                if limit is not None and quantity < limit:
                    report_path_for_ingredients = self.make_report_directory()
                    file_path = os.path.join(report_path_for_ingredients, "Reports_to_the_head_of_the_trade")
                    if not os.path.exists(file_path):
                        os.mkdir(file_path)
                    file_name = f"report_{report_number}_{ingredient}_minimum.txt"
                    file_path_with_name = os.path.join(file_path, file_name)
                    if not os.path.exists(file_path_with_name):
                        with open(file_path_with_name, "w") as file:
                            file.write(f"Report\n The {ingredient} are below the minimum limit, "
                                       f"please order this ingredient\n"
                                       f"This report is send on the {datetime.now()}")
                        print(f"The quantity of the {ingredient} is running low.")
                        file_exists = False
                    else:
                        report_number += 1
                elif limit is None and quantity < 1000:
                    report_path_for_ingredients = self.make_report_directory()
                    file_path = os.path.join(report_path_for_ingredients, "Reports_to_the_head_of_the_trade")
                    if not os.path.exists(file_path):
                        os.mkdir(file_path)
                    file_name = f"report_{report_number}_{ingredient}_minimum.txt"
                    file_path_with_name = os.path.join(file_path, file_name)
                    if not os.path.exists(file_path_with_name):
                        with open(file_path_with_name, "w") as file:
                            file.write(f"Report\n The {ingredient} are below the minimum limit, "
                                       f"please order this ingredient\n"
                                       f"This report is send on the {datetime.now()}")
                        print(f"The quantity of the {ingredient} is running low.")
                        file_exists = False
                    else:
                        report_number += 1
                else:
                    file_exists = False
            report_number = 1

    def add_ingredients_by_recipe(self, recipe_name, number_of_ice_creams):
        """Add ingredients to the warehouse based on a recipe and the number of ice creams to be made."""
        with open(os.path.join("recipes", recipe_name + ".txt"), "r") as file:
            ingredients = {}
            for line in file:
                line = line.strip().split(": ")
                ingredient = line[0]
                quantity = line[1:2]
                for element in quantity:
                    ingredients[ingredient] = int(element.split(" ")[0])

        factory = Factory(recipe_name)
        for ingredient, quantity in factory.scale_recipe(number_of_ice_creams).items():
            total_quantity = quantity
            self.buy_ingredients(ingredient, total_quantity)
        print("Ingredients added successfully.")

    @staticmethod
    def ingredients_needed_for_recipe(recipe_name):
        """Check ingredients and quantities needed for given recipe."""
        with open(os.path.join("recipes", recipe_name + ".txt"), "r") as file:
            ingredients = {}
            for line in file:
                line = line.strip().split(": ")
                ingredient = line[0]
                quantity = line[1:2]
                for element in quantity:
                    ingredients[ingredient] = int(element.split(" ")[0])
        return ingredients

    def check_ingredients_for_all_recipes(self):
        """Check which ice cream can be produced based on the ingredients in the warehouse."""
        for recipe in os.listdir("recipes"):
            recipe_name = recipe.split(".")[0]
            factory = Factory(recipe_name)
            ingredients = self.ingredients_needed_for_recipe(recipe_name)
            for ingredient, quantity in ingredients.items():
                if ingredient not in self.ingredients:
                    print(
                        f"We do not have enough ingredient in the warehouse to produce any {recipe_name} ice creams.")
                    break
                else:
                    ice_creams_possible = self.ingredients[ingredient] // quantity * factory.total_by_recipe
            else:
                print(f"We have enough ingredients in the warehouse to produce "
                      f"{ice_creams_possible} {recipe_name} ice cream!")

    def add_ice_cream(self, ice_cream, quantity):
        """Add produced ice cream to the warehouse."""
        if ice_cream in self.ice_creams:
            self.ice_creams[ice_cream] += quantity
        else:
            self.ice_creams[ice_cream] = quantity

    def sell_ice_cream(self, quantity: int, ice_cream=None):
        """Sell ice cream from the warehouse."""
        if ice_cream is not None:
            for ice_cream in self.ice_creams:
                if self.ice_creams[ice_cream] >= quantity:
                    self.ice_creams[ice_cream] -= quantity
                    print("ice cream sold")
                else:
                    print(f"We don't have that much of {ice_cream}")

    def report_for_ice_creams(self):
        """Create report if quantity of ice creams in the warehouse are below limit.
            Report is saved in Reports/Reports_to_the_head_of_the_production and have unique number."""
        report_number = 1
        for ice_cream, quantity in self.ice_creams.items():
            if quantity < 20:
                report_path_for_ice_cream = self.make_report_directory()
                file_path = os.path.join(report_path_for_ice_cream, "Reports_to_the_head_of_the_production")
                if not os.path.exists(file_path):
                    os.mkdir(file_path)
                file_exists = True
                while file_exists:
                    file_name = f"report_{report_number}_{ice_cream}_minimum.txt"
                    file_path_with_name = os.path.join(file_path, file_name)
                    if not os.path.exists(file_path_with_name):
                        with open(file_path_with_name, "w") as file:
                            file.write(
                                f"Report\n The {ice_cream} are below the minimum limit, please make this ice cream\n"
                                f"This report is send on the {datetime.now()}")
                        print(f"The quantity of the {ice_cream} are below the minimum limit, please make more")
                        file_exists = False
                    else:
                        report_number += 1
                report_number = 1

    @staticmethod
    def create_new_recipe(recipe_name):
        """Create new recipe with users input which contains: ingredient and quantity."""
        try:
            new_ingredients = {}
            print("Enter the ingredients for the recipe in the following format: ingredient_name: quantity")
            print("Type 'done' when you are finished entering ingredients.")
            add_ingredients = input("Enter ingredient: ")
            while add_ingredients != "done":
                ingredient_parts = add_ingredients.split(": ")
                ingredient = ingredient_parts[0]
                quantity = ingredient_parts[1]
                new_ingredients[ingredient] = quantity
                add_ingredients = input("Enter ingredient: ")

                with open(os.path.join("recipes", f"{recipe_name}.txt"), "w") as file:
                    file.write(f"{recipe_name}\n")
                    for ingredient, quantity in new_ingredients.items():
                        file.write(f"{ingredient}: {quantity}\n")
        except IndexError:
            print("Invalid input please follow the instructions ingredient_name: quantity")

    def amount_of_king_and_capri(self, ice_cream_name):
        """Check the amount of ice creams king and capri in the warehouse."""
        if ice_cream_name in self.ice_creams:
            return self.ice_creams[ice_cream_name]
        else:
            return 0

    def check_cocoa(self):
        """Check the quantity of cocoa in the warehouse and calculate how many choco-moco can be made with it."""
        if "cocoa" in self.ingredients:
            choco_moco_ingredients = self.ingredients_needed_for_recipe("choco_moco")
            cocoa_needed = choco_moco_ingredients["cocoa"]
            cocoa_in_warehouse = self.ingredients["cocoa"]
            how_many_choco_moco = cocoa_in_warehouse // cocoa_needed
            print(f"There are {cocoa_in_warehouse} grams of cocoa in the warehouse. "
                  f"Using this, we can produce {how_many_choco_moco} choco_moco ice creams.")
        else:
            print("There is no cocoa in the warehouse")
