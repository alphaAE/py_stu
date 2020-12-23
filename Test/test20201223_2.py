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
            tmpData.append(row.replace("\n", "").split(","))
        return tmpData


def read(file):
    with open(file, "r", encoding="UTF8", newline='') as f:
        tmpData = list()
        for row in f.readlines():
            tmpData.append(row)
        return tmpData


data = read("./OutFile/data.txt")
# 二次处理
data = [d.replace("\n", "").replace("\r", "").split("|") for d in data]
print(data)
saveCsv("./OutFile/data.csv", data)

# 读取Csv并另存为
dataRead = readCsv("./OutFile/data.csv")
print(dataRead)
saveCsv("./OutFile/data2.csv", dataRead)
