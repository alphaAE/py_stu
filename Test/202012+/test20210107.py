import random

# 1 源数据删除去重
# numList = [i for i in range(0, 10)]
# pwd = ""
# for i in range(8):
#     a = random.choice(numList)
#     numList.remove(a)
#     pwd += str(a)
# print(pwd)

# 2 set去重
# numList = [i for i in range(0, 10)]
# pwdSet = set()
# while len(pwdSet) < 8:
#     pwdSet.add(str(random.choice(numList)))
# pwdStr = ''.join(pwdSet)
# print(pwdStr)

# 3 无需多言
print(''.join([str(i) for i in random.sample([i for i in range(0, 10)], 7)]))
