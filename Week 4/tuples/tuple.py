def student():
    print("Enter your name:")
    name = input()
    print("What is your age?")
    age = int(input())
    print("Do you have a dog?")
    dog = input()

    if dog == 'yes':
        dog_bool = True
    else:
        dog_bool = False
    return name, age, dog_bool


# generate more students

print("How many students to generate?")
n = int(input())
i = 0

all_students = []

while ( i < n ):
    # saving the return from tuple in an variable ( temp ?? )
    obj = student()
    # Append the temp variable into a new one to return the result
    all_students.append(obj)
    i += 1
print(all_students)

