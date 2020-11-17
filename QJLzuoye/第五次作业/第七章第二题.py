#打开文件
try:
    with open(r"D:\Jane Eyre.txt",'r') as f:
        text=f.read()
        text=text.lower()                           #小写
        O1=[',','.',';','-',':','\'','"','?']       #屏蔽标点
        O2=['the','and','to','of','a','be','it','is','not','but']   
                                                    #屏蔽一些词
        for c in O1:                                #屏蔽标点
            text=text.replace(c,' ')
        words=text.split()                          #空格分词

        counts={}
        for w in words:
            counts[w]=counts.get(w,0)+1             #统计个数
        for c in O2:                                #屏蔽一些词
            del counts[c]
        l=list(counts.items())                      #字典转为列表
        l.sort(key=lambda x:x[1],reverse=True)      #排序列表
        l2=l[:10]                                   #取前10个
except IOError:
    print("打开失败")
else:
    print("读取分析成功")

try:
#打开（生成）词频文件
    with open(r'D:\Jane Eyre freq.txt','w+') as f:
        for i in l2:
            f.write(str(i[0])+'\t'+str(i[1])+'\n')  #写入
except IOError:
    print("写入失败")
else:
    print("输出文件成功：D:\Jane Eyre freq.txt")

