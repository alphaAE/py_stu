

def decToBin(num):
    outStr = ""
    while num > 0:
        num, mod = divmod(num, 2)
        outStr += str(mod)
    return "0b" + outStr[::-1]


def decToHex(num):
    staticStrLib = ['A', 'B', 'C', 'D', 'E', 'F']
    outStr = ""
    while num > 0:
        num, mod = divmod(num, 16)
        if mod > 9 and mod < 16:
            mod = staticStrLib[mod - 10]
        outStr += str(mod)
    return "0x" + outStr[::-1]


while True:
    base = input("输入(进制): ")
    num = input("输入(数值): ")
    if base in ['B']:
        print(decToBin(int(num)), bin(int(num)))
    elif base in ['H']:
        print(decToHex(int(num)), hex(int(num)))
