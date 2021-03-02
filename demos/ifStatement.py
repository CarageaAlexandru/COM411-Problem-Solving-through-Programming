print("What is your name?")

name = input()

print("Do you have a dog? (True or false)")

dog = input()

if len(name) > 9 and dog == "True":
    print("You have a very loooong name")
    print("Your name contains {} letters".format(len(name)))
else:
    print("Your name is quite okay")

print("this is the END of the program")