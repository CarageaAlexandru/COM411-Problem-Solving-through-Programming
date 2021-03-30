dictionary1 = {}
dictionary2 = {
    "name": "Piotr",
    "age": 26,
    "allergy": ["coffee ", "hard working"]
}

# appending to a dictionary

dictionary2["sibblings"] = 2


menu = {
	1: "Start",
	2: "Find a planet", 
	3: "Enter a new Planet"
}

print(menu[int(input("Enter 1, 2, or 3\n"))])