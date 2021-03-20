answer = input("Where should I look?\n")

if ( answer == "in the bedroom" ):
    answer = input("Where in the bedroom should I look?\n")
    if ( answer == "under the bed" ):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")
elif ( answer == "in the bathroom" ):
    anwer = input("Where in the bathroom should I look?\n")
    if ( answer == "in the bathtub\n" ):
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")
elif ( answer == "in the lab" ):
    answer = input("Where in the lab should I look?\n")
    if ( answer == "on the table" ):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")
else:
    print("I do not know where that is but I will keep looking.")