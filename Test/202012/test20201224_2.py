# 导入依赖库
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 获取文本


def get_text():
    txt = open("./OutFIle/sanguo.txt", encoding='utf8').read()
    txt = txt.lower()
    # 将文本中的符号替换为空格
    for ch in '：，、。《》“” ---':
        txt = txt.replace(ch, " ")

    return txt


# 词频统计
three_txt = get_text()
words = three_txt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
finall = ""
for i in range(74567):
    word, count = items[i]
    # print("{0:<10}{1:>5}".format(word, count))
    finall += (word + ' ') * count

print(len(items))

wc = WordCloud(
    # 设置字体，不指定就会出现乱码
    font_path="msyh.ttc",
    # 设置背景色
    background_color='white',
    # 设置背景宽
    width=1080,
    # 设置背景高
    height=1920,
    max_font_size=200,
    mode='RGBA',
    max_words=74567,
    collocations=False
    # colormap='pink'
)
# 产生词云
wc.generate(finall)


# 5、显示
# 指定所绘图名称
plt.figure("three")
# 以图片的形式显示词云
plt.imshow(wc)
# 关闭图像坐标系
plt.axis("off")
plt.show()
