import jieba
import os
import wordcloud
from imageio import imread

os.chdir('D:\\')
def stopwordslist(path):
    stopwords=[line.strip() for line in open(path, 'r').readlines()]
    return stopwords
def wordfreq(path, text, topn):
    #jieba.add_word('马保国')
    #jieba.add_word('混元功法')
    words = jieba.lcut(text.strip())
    counts={}
    stopwords=stopwordslist('三国演义stop_words.txt')
    for word in words:
        if len(word)==1:
            continue
        elif word not in stopwords:
            counts[word]=counts.get(word,0)+1
    items=list(counts.items())
    items.sort(key=lambda x :x[1], reverse=True)
    f=open(path+'三国演义_词频.txt', 'w')
    for i in range(topn):
        word,count=items[i]
        f.writelines("{}\t{}\n".format(word,count))
    f.close()
f=open('三国演义.txt', 'r',encoding='utf8')
text=f.read()
f.close()
wordfreq('D:\\', text, 200 )

f=open('三国演义_词频.txt', 'r')
text=f.read()
f.close
bg_pic=imread('三国mask.png')
wcloud=wordcloud.WordCloud(font_path= r'C:\Windows\Fonts\simhei.ttf',\
background_color = "white", #width=1000,\
max_words=500,\
mask=bg_pic,\
max_font_size=100,\
#height=1000,\
margin=1).generate(text)
wcloud.to_file('三国演义cloud.png')
