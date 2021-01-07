import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def saveCsv(file, data):
    with open(file, "w", encoding="UTF8", newline='') as f:
        for row in data:
            _str = ",".join(map(str, row))
            f.write(_str + "\n")
    print("Save Success.")


def readCsv(file):
    with open(file, "r", encoding="UTF8", newline='') as f:
        tmpData = list()
        for row in f.readlines():
            tmpData.append(row.replace("\n", "").replace("\r", "").split(","))
        return tmpData


# 读取Csv字典
dataRead = readCsv("./OutFile/word.csv")
# 抛出头
header = dataRead.pop(0)
print(dataRead)
# saveCsv("./OutFile/data2.csv", dataRead)
