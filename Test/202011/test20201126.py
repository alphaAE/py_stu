import numpy as np

# print(np.arange(10))
# print(np.arange(0, 10, 2))
# print(np.arange(1, 10, 3))
# print()

# listA = list(range(1, 8, 2))
# arrayA = np.array(listA)
# print(listA, arrayA)
# print(type(listA), type(arrayA))

randArr = np.random.randint(10, 20, (6, 4), dtype=np.int32)
print(randArr)

zeroArr = np.zeros((3, 4), dtype=np.int32)
print(zeroArr)

oneArr = np.ones((4, 3), dtype=np.int32)
print(oneArr)
