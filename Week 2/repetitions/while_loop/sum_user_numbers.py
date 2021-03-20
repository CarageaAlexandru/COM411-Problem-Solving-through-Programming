numbers = int(input("How many numbers should I sum up?\n"))
sum = 0

x = 1

while (x <= numbers) :
    num = int(input(f"Please insert number {x} of number {numbers}\n"))
    sum = sum + num;

    x += 1

print(sum)