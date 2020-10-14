# for i in range(1, 10):
#     for j in range(1, 10):
#         if i>=j:
#             print("{:2} *{:2} ={:2}  ".format(i, j, i*j), end="")
#     print()


# def printTriangle(line):
#     for i in range(line):
#         print("{}{}".format(' '*(line - i), '*'*(i * 2 + 1)))

# printTriangle(21)

#       1
#     3   5
#   7   9   11




###
nowEffectiveness = 1.0

oneYearEffectiveness = pow((1.0 + 0.01), 365)
print("若一年都为1%: {}".format(oneYearEffectiveness))


### 1 - 1000内的回文
for i in range(1,1001):
    if str(i)[::-1] == str(i):
        print(i, end=" ")
    
