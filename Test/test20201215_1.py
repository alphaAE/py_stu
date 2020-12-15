import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 用来正常显示中文
plt.rcParams["font.sans-serif"] = ["SimHei"]
# 用来正常显示负号
plt.rcParams["axes.unicode_minus"] = False

# 文件打开 读取到变量 关闭
tmpFile = open("./Test/shiguang.txt", "r", encoding="utf-8")
txt = tmpFile.read()
tmpFile.close()

# 对文章切片
words = jieba.lcut(txt)
words_all = ' '.join(words)

# width,height,margin可以设置图片属性
# generate 可以对全部文本进行自动分词,但是对中文支持不好
# 可以设置font_path参数来设置字体集
# background_color参数为设置背景颜色,默认颜色为黑色
wordcloud = WordCloud(background_color="white",
                      width=1000, height=860, margin=2)

# 词云对象加入分析句子的来源
wordcloud.generate(words_all)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# wordcloud.to_file('./Test/wordcloud.png')
# 保存图片,但是在第三模块的例子中 图片大小将会按照 mask 保存
