# 更名多级目录的TXT文本
import os

path = r"C:\Users\AlphaAE\Desktop\root"

print(os.walk(path).__next__())

for root, dirs, files in os.walk(path):
    for fileName in files:
        pass
        # print(os.path.join(root, fileName))

