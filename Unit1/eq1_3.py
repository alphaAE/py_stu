for i in range(1, 11):
    for j in range(1, i + 1):
        print("{} * {} = {:2}  ".format(i, j, i*j), end="")
    print()