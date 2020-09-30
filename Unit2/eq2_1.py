
tempType = input("in temp type(C/F):")
tempNum = eval(input("in temp(Num):"))

if tempType in ['C', 'c']:
    fOut = 1.8 * tempNum + 32
    print("to F: {:.2f}F".format(fOut))
elif tempType in ['F', 'f']:
    cOut = (tempNum - 32) / 1.8
    print("to C: {:.2f}C".format(cOut))
else:
    print("Err: temp type error!")