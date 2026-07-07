def main():


    fruits = {
         "apple": "130",
         "Avocado":"50",
         "Banana":"110",
         "Cantaloupe":"50",
         "Grapefruit":"60",
         "Grapes":"90",
         "Homeydew Melon":"50",
         "Kiwifruit":"90",
         "Lemon":"15",
         "Lime":"20",
         "Orange":"80",
         "pear":"100",
         "Peach":"60",
         "Strawberries":"50",
         "Sweet Cherries":"100",
         "Tangerine":"50",
         "Watermelon":"80"
         }
    item = input("Item: ")
    if item in fruits:
        print("Calories:",fruits[item])
main()
