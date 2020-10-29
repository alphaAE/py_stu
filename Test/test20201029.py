### 重庆例子嵌套字典
dictCity = {
    "重庆": {
        "沙坪坝": ["三峡广场", "观音桥", "大学城"],
        "渝北": ["空港", "双龙"]
    }
}

print(dictCity)
print(dictCity["重庆"]["沙坪坝"])

listCity = list(dictCity.items())
print(listCity)
