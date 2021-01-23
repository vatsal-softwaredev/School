string = "Delhi Public School Ghaziabad"

freq = {}

for i in string.lower():
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("Count of all characters in Delhi Public School Ghaziabad is :\n ", str(freq))
