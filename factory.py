import os
from datetime import datetime

PATH = os.getcwd()


class Factory:
    """Model for class Factory."""
    def __init__(self, ice_cream_name, total_by_recipe: int = 10):
        """Initialize factory instance. """
        self.ingredients = {}
        folder_name = "recipes"
        file_name = os.path.join(f"{folder_name}/{ice_cream_name}.txt")

        with open(file_name, "r") as f:
            lines = f.readlines()
            self.name = lines[0].strip()

            for line in lines[1:]:
                ingredient = line.strip().split(": ")[0]
                quantity = line.strip().split(": ")[1:2]
                for element in quantity:
                    self.ingredients[ingredient] = int(element.split(" ")[0])

        self.total_by_recipe = total_by_recipe

    def scale_recipe(self, new_total: int):
        """Scale ingredients in the recipe to the desired number of ice creams"""
        if new_total == self.total_by_recipe:
            scaling_factor = 1
        else:
            scaling_factor = new_total / self.total_by_recipe
        for ingredient, quantity in self.ingredients.items():
            self.ingredients[ingredient] = quantity * scaling_factor
        return self.ingredients

    @staticmethod
    def make_products_directory():
        """Creating directory for storing Production reports if it does not already exist."""
        product_path = os.path.join(PATH, "Products")
        if not os.path.exists(product_path):
            os.mkdir(product_path)
        return product_path

    def produce_ice_creams(self, warehouse, number_of_ice_creams):
        """Producing ice creams and writing production reports."""
        produce_number = 1
        self.scale_recipe(number_of_ice_creams)
        produce_path = self.make_products_directory()
        if not os.path.exists(produce_path):
            os.mkdir(produce_path)
        file_path = f"produced_ice_cream_{produce_number}.txt"
        while os.path.exists(os.path.join(produce_path, file_path)):
            produce_number += 1
            file_path = f"produced_ice_cream_{produce_number}.txt"
        if warehouse.has_ingredients(self.ingredients):
            warehouse.use_ingredient(self.ingredients)
            warehouse.add_ice_cream(self.name, number_of_ice_creams)
            with open(os.path.join(produce_path, file_path), "w") as file:
                file.write(f"{self.name}, {number_of_ice_creams}\n")
                for ingredient, quantity in self.ingredients.items():
                    file.write(f"{ingredient}: {quantity}\n")
                file.write(f"production was completed and the ice cream was sent to warehouses on {datetime.now()}")
            return True
        else:
            warehouse.check_ingredients_for_all_recipes()
            return False
