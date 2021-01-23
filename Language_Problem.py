Language = {"java": 100, "python": 200, "C++": 500}

values = Language.values()
no = 0
for value in values:
    if value > 100:
        print(list(Language.items())[no])
    no += 1
