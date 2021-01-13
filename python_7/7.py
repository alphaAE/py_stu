# 写txt
with open('./out.txt','w',encoding='utf8') as _file:
    _file.write("a,s,d,f,g\n")
    _file.write("1,3,4,5,6\n")

# 读txt
with open('./out.txt','r',encoding='utf8') as _file:
    _str = _file.read()
    print(_str)

import csv

# 读txt写cvs
with open('./out.txt','r',encoding='utf8') as _file:
    dataList = list()
    for line in _file.readlines():
        dataList.append(line.replace('\n','').split(','))
    print(dataList)
    with open('./out.csv','w',encoding='utf8', newline = '') as _file2:
        csv_writer = csv.writer(_file2)
        csv_writer.writerows(dataList)

# 读cvs
with open('./out.csv','r',encoding='utf8', newline = '') as _file2:
    csv_reader = csv.reader(_file2)
    for row in csv_reader:
        print(row)
