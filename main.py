import sys
from warehouse import Warehouse
from factory import Factory

warehouse = Warehouse()


def main():
    print("a: Add ingredient and amount of ingredient to the warehouse.")
    print("b: Print ingredients and their amount in the warehouse.")
    print("c: Add all ingredients and their quantity from recipe according "
          "to the number of ice creams that can be made from it.")
    print("d: Produce ice cream")
    print("e: Print ice creams and their amount in warehouse.")
    print("f: Sell ice cream from warehouse")
    print("g: Add new recipe.")
    print("h: Number of king and capri ice creams in the warehouse.")
    print("i: Check amount of cocoa and how many choco-moco can be produced with that amount.")

    while True:
        try:
            option = input("Please select option that you want: a/b/c/d/e/f/g/h/i: ")

            if option == "a":
                ingredient_name = input("Please enter ingredient name: ")
                quantity_of_ingredient = int(input("Please enter the amount of this ingredient: "))
                warehouse.buy_ingredients(ingredient_name, quantity_of_ingredient)
                warehouse.report_for_ingredients()

            elif option == "b":
                warehouse.print_ingredients()

            elif option == "c":
                recipe_name = input("Enter recipe name that you want: ")
                number_of_ice_creams = int(input("Enter the desired number of ice creams: "))
                warehouse.add_ingredients_by_recipe(recipe_name, number_of_ice_creams)
                warehouse.report_for_ingredients()

            elif option == "d":
                ice_cream_name = input("Enter the name of ice cream recipe that you want to produce: ")
                number_of_ice_creams = int(input("Enter the number of ice creams that you want to produce: "))
                factory = Factory(ice_cream_name)
                if factory.produce_ice_creams(warehouse, number_of_ice_creams):
                    print(f"Successfully produced {number_of_ice_creams} {ice_cream_name} ice creams!")
                    warehouse.report_for_ingredients()
                    warehouse.report_for_ice_creams()
                else:
                    produce = input("Do you want to produce another ice cream that is possible"
                                    " to produce with available ingredients (yes/no)? ")

                    if produce == "yes":
                        ice_cream_name = input("Enter the name of ice cream that you want to produce: ")
                        number_of_ice_creams = int(input("Enter the number of ice creams that you want to produce: "))
                        factory = Factory(ice_cream_name)
                        if factory.produce_ice_creams(warehouse, number_of_ice_creams):
                            print(f"Successfully produced {number_of_ice_creams} {ice_cream_name} ice creams!")
                            warehouse.report_for_ingredients()
                            warehouse.report_for_ice_creams()

                    elif produce == "no":
                        pass

            elif option == "e":
                warehouse.print_ice_creams()

            elif option == "f":
                name = input("Enter the name of the ice cream that you want to sell: ")
                number_of_ice_creams = int(input("Enter the number of the ice creams: "))
                warehouse.sell_ice_cream(number_of_ice_creams, name)
                warehouse.report_for_ice_creams()

            elif option == "g":
                recipe_name = input("Enter the name of new recipe: ")
                warehouse.create_new_recipe(recipe_name)

            elif option == "h":
                number_of_capri = warehouse.amount_of_king_and_capri("Capri")
                number_of_king = warehouse.amount_of_king_and_capri("King")
                print(f"There are {number_of_capri} capri ice creams in the warehouse.")
                print(f"There are {number_of_king} king ice creams in the warehouse.")

            elif option == "i":
                warehouse.check_cocoa()

            elif option == "exit":
                sys.exit()
        except ValueError:
            print("Invalid input, please try again")
        except FileNotFoundError:
            print("Invalid input, please try again")


if __name__ == '__main__':
    main()
