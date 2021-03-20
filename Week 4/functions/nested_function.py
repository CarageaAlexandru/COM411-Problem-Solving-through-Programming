def get_me_fruits():
    fruits = []
    n = int(input("How many fruits would you like to enter?\n"))

    for i in range(n):
        print("Please enter the fruit you want to add.")
        fruits.append(input())

    return fruits

def get_fruits():
    fruits = ["apple", "kiwi", "banana", "mango", "pear", "pineapple"]
    fruits2 = get_me_fruits()

    print(f"Your fruits are {fruits}")    

    print(f"The second list with the fruits is {fruits2}")

get_fruits()