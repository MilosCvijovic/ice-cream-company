This project (Ice Cream Company) was done as homework in the IT Bootcamp
course (basics of web programming).

Environment that I used for this project is Python 3.10

Packages that need to be imported:
    os
    datetime
    sys

Ice cream company project works with users input, because the warehouse is empty 
(it doesn't have any ingredients and ice creams). First thing that should be done is adding the
ingredients with (options a or c), then you can print the amount of ingredients in the warehouse
(option b), or you can produce ice cream with (option d). You can also add a new recipe at the beginning
using (option g). When you have produced ice creams you can print the amount of ice creams in warehouse 
(option e) or sell some amount of ice cream with (option f). At the end you have (option h) to check how many 
king and capri ice creams are in the warehouse, (option i) to check the amount of cocoa that is in the warehouse 
and how many choco-moco ice cream you can make with that amount. 
There are also methods to check the amount of ingredients and ice creams
in the warehouse. These methods will work after you add ingredients and produce ice cream. They send reports when some 
ingredient or ice cream are below minimum limit. These reports are saved in directory 'reports' and have:
1. 'reports to the head of the production' directory where the reports are saved when the ice cream limits are under the
minimum.
2. 'reports to the head of the trade' directory where the reports are saved when ingredient limits are under minimum.
Method that save reports to 'products' directory when the ice cream is made. Reports include names and the amount
of ice cream that was made and spent ingredients.


Options
    'a' - Add new ingredient and amount of ingredients or increases existing ones in the warehouse 
        input(Please enter ingredient name) Enter the name of the ingredient that you want to add or increase
        input(Please enter how much of this ingredient would you like) Enter amount of ingredient that you want(integer)
    'b' - Prints ingredients and amount of ingredients in the warehouse
    'c' - Add ingredients and amount of ingredients or increases existing ones in the warehouse according to the amount 
        of ice cream you want to make.
        input(Enter recipe name that you want) Enter recipe name that exists in directory recipes or name of the new 
            recipe that you added.
        input(Enter the desired number of ice creams) Enter the desired number of ice creams that you want to produce.
            (integer)
    'd' - Produces ice creams with ingredients from the warehouse, if there isn't enough ingredients in warehouse check
        other recipes and amount of ingredients to see which ice cream can be made.
        input(Enter the name of ice cream recipe that you want to produce) Enter the name of recipe that exists in 
            directory recipes. 
        input(Enter the number of ice creams that you want to produce) Enter desired number of ice creams (integer).
    'e' - Print ice creams and amount of ice creams in warehouse.
    'f' - Sell ice creams from warehouse.
        input(Enter the name of the ice cream that you want to sell) Enter the name of produced ice cream.
        input(Enter the number of the ice creams) Enter number of ice creams (integer).
    'g' - Make new recipe, add name that be saved in directory recipes (name.txt) and ingredients and amount of 
            ingredients
        input(Enter the name of new recipe) Enter the name of new recipe.
        input(Enter the ingredients for the recipe in the following format: ingredient_name: quantity) 
            Enter the ingredient name and quantity according to the given format (ingredient: quantity)
            This will repeat until you enter 'done'. Then your new recipe will be saved.
    'h' - Prints amount of king and capri ice cream in warehouse
    'i' - Prints amount of cocoa and how many choco-moco ice cream can be made with that amount.
    'exit' - close the application















