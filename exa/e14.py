# 7-14 CSV格式向JSON格式的转换
import json
fr = open("./OutFile/data.csv", "r")
ls = []
for line in fr:
    line = line.replace("\n", "")
    ls.append(line.split(','))
fr.close()
fw = open("./OutFile/data.json", "w")
for i in range(1, len(ls)):
    ls[i] = dict(zip(ls[0], ls[i]))
json.dump(ls[1:], fw, sort_keys=True, indent=4, ensure_ascii=False)
fw.close()
