# Asking for the Number of Entries:
n = int(input("Please Enter the Number of Entries: "))

# Default PhoneBook:
PhoneBook = {}

# Adding Names and Number in Dictionary:
for i in range(n):
    name = input("Please Enter the Name: ")
    number = int(input("Please Enter the Number: "))
    PhoneBook[name] = number

# Asking for Name:
find = input("Enter the Name: ")

# Finding the Number:
print("The Number is :", PhoneBook.get(find))
