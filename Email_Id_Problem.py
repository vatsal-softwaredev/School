# Asking for the Number of Entries:
n = int(input("Please Enter the Number of Entries: "))

# Default Tuples
emails = []
username = []
domain = []


for i in range(n):
    # Entering Email IDs:
    elements = input()
    # Splitting the Email into Username and Domain Name
    user = elements.split("@")
    # Adding Username in Tuple
    username.append(user[0])
    # Adding Domain in Tuple
    domain.append(user[1])
    # Adding Email in Tuple
    emails.append(elements)

# Printing all three
print("Email IDs:")
print(emails)
print("Username:")
print(username)
print("Domain Name:")
print(domain)
