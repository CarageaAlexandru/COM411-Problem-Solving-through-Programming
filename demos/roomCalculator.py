# Code that can be used to calculate the total cost of room makeover in a house

def room_area(width, length):
    return width*length

def room_name():
    print("What is the name of the room?")
    return input()

def price(name, area):
    if name == "bathroom":
        return 20*area
    elif name == "kitchen":
        return 10*area
    elif name == "bedroom":
        return 5*area
    else: 
        return 7*area

def run():
    name = room_name()
    print("What is the width of the room?")
    width = float(input())
    print("What is the length of the room?")
    length = float(input())
    print(f"You should pay £{price(name,room_area(width,length))}")

run()



# it is not recommended to import full files if we are not going to use them
# instead import just the function

#import demos.roomCalculator as roomCalculator # imports full file with all the function

# from roomCalculator import run,room_name # imports just the functions

#roomCalculator.run()