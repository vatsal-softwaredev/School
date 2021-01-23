# Asking for the Number of Entries:
n = int(input("Please Enter the Number of Entries: "))

# Default Tuple
names = []

for i in range(n):
    # Asking the Names of Students:
    name = input("Enter the Name: ")
    # Adding it into the Tuple
    names.append(name)

# Printing the Names of Students:
print("Names of all Students are: ", names)
attend = input("Enter the name of the Student: ")

# Checking if Present or Not:
if any(attend in i for i in names):
    print(attend, "is Present in the Tuple")
else:
    print(attend, "is Not Present in the Tuple")
