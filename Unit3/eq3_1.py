#

bodyWeight = 50.0

for i in range(10):
    bodyWeight += 0.5
    print("第 {} 年的月球体重是：{:.5f}.".format(i + 1, bodyWeight * 0.165))
