password = input("Enter Password: ")
num_of_asterisks = len(password)
while num_of_asterisks <= 0:
    print("Invalid Password")
    password = input("Enter Password: ")
    num_of_asterisks = len(password)

print(num_of_asterisks * "*")


