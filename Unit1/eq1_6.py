diet = ["A", "B", "C", "D", "E"]

for x in diet:
    for y in diet:
        if x != y:
            print("{}&{}".format(x, y))