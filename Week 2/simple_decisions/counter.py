num1 = int(input("Please enter first number\n"))
num2 = int(input("Please enter second number\n"))
num3 = int(input("Please enter third number\n"))

odd_numbers = []
even_numbers = []

if ( num1 % 2 == 0 ):
    even_numbers.append(num1)
elif ( num1 % 2 != 0 ):
    odd_numbers.append(num1)


if ( num2 % 2 == 0 ):
    even_numbers.append(num2)
elif ( num2 % 2 != 0 ):
    odd_numbers.append(num2)


if ( num3 % 2 == 0 ):
    even_numbers.append(num3)
elif ( num3 % 2 != 0 ):
    odd_numbers.append(num3)


print(f"These are the odd numbers: {len(odd_numbers)}")
print(f"These are the even numbers: {len(even_numbers)}")

print(f"Your even numbers are {even_numbers}.")
print(f"Your odd numbers are {odd_numbers}.")
