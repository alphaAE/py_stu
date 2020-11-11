
import jieba
# 文件打开 读取到变量 关闭
tmpFile = open("./Test/shiguang.txt", "r", encoding="utf-8")
txt = tmpFile.read()
tmpFile.close()

# 对文章切片
words = jieba.lcut(txt)
counts = {}

# 遍历切片后的字词列表统计个数
for word in words:
    # 屏蔽2个字以下的字词
    if len(word) >= 2:
        counts[word] = counts.get(word, 0) + 1

# 转换为list为排序做准备
items = list(counts.items())

# 使用每一个item的[1]项进行降序排序
items.sort(key=lambda a: a[1], reverse=True)

# 输出排序后的前十项目
for i in range(10):
    word, count = items[i]
    print("{} : {}".format(word, count))

