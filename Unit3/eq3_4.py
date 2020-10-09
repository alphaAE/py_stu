
try:

    while True:
   
        numStr = input("in Num: ")

        # print(numStr[::-1])
        # print(numStr[0: int(len(numStr) / 2)])
        # print(numStr[-1: -int(len(numStr) / 2) - 1: -1])

        if numStr[0: len(numStr) / 2)] == numStr[-1: -len(numStr) / 2 - 1: -1]:
            print("回文！")
        else:
            print("非回文！")

except:
    print("Error")