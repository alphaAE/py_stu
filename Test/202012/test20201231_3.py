

def factorList(num):
    fList = list()
    for i in range(1, num):
        if num % i == 0:
            fList.append(i)
    return fList


for n in range(1, 1001):
    fList = factorList(n)
    _sum = sum(fList)
    if _sum == n:
        print("{} = {}".format(n, " + ".join([str(i) for i in fList])))
