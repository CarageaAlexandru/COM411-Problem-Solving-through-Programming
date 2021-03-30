phonebook = {

}

while True:
	name = input("Enter the name: ")
	number = input("Enter the number: ")
	phonebook[name] = number

	if input("Type 'x' to stop.") == 'x':
		break

def calling(string, book = {}):
	print(f"Calling {string} with a phone number {book[string]}")

calling("Piotr", phonebook)