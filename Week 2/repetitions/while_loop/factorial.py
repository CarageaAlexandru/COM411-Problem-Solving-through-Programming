number = int(input("Please enter the number for factorial.\n"));

factorial = 1

while ( number > 1 ):
    factorial = factorial * number
    number = number - 1

print(factorial)