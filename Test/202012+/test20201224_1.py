# 词云
import jieba
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

tmpFile = open("./OutFile/sanguo.txt", "r", encoding="utf-8")
txt = tmpFile.read()
tmpFile.close()

words = jieba.lcut(txt)
words2 = list()
for word in words:
    # 屏蔽2个字以下的字词
    if len(word) >= 2:
        words2.append(word)

words_all = ' '.join(words2)

wordcloud = WordCloud(background_color="white", width=1920,
                      height=1080, margin=2, font_path="./simhei",
                      min_font_size=4, max_font_size=300, max_words=3000 ,collocations=False)
wordcloud.generate(words_all)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
