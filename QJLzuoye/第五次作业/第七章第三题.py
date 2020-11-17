
try:
    dic={}
    with open(r'D:\result.txt','r+') as f:
        text=f.read()
        text=text.split()
        # for i in text:
        #     f.write(i+' ')






        for i in text:
            dic[i]=dic.get(i,0)+1
        f.write('\n')
        for k,v in dic.items():
            f.write(str(k)+'\t'+str(v)+'\n')
except IOError:
    print('文件读取失败')
else:
    print('分析成功')