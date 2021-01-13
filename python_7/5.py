# 字符串特殊方法

# 进度条
import time
for i in range(1, 101):
    print("\r {} {} {}%".format('=' * i, '-' * (100 - i), i), end='')
    time.sleep(0.01)
print()

# 凯撒密码
pwd = 'asd1235gf'
enPwd = ''
dePwd = ''
for i in pwd:
    enPwd += chr(ord(i) + 1)
for i in enPwd:
    dePwd += chr(ord(i) - 1)
print(enPwd, dePwd)

# 文本切割
_str = "1 1 23 3 53 a fg"
print(_str.rsplit(' '))
