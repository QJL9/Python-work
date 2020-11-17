import csv

#以下是第五章习题的部分代码：
dicTXL={"小新":[13913000001,18191220001],"小亮":[13913000002,18191220002],"小刚":[13913000003,18191220003]}
dicother={"大刘":[13914000001,18191230001],"大王":[13914000002,181191230002],"大张":[13914000003,181191230003]}
dicTXL.update(dicother)
print(dicTXL)
dicWX={"小新":'xx9907',"小刚":'gang1004',"大王":'jack_w',"大刘":'liu666'}

for i in dicWX.keys():
    dicTXL[i]=[dicTXL[i][0],dicTXL[i][0],dicWX[i]]
print(dicTXL)
dicTXL["大王"][0]=13914000004
#到此结束，生成了dicTXL字典

#字典转换为列表
ldicTXL=[]
for k,v in dicTXL.items():
    v.insert(0,k)
    ldicTXL.append(v)
print(ldicTXL)

#写入文件
try:
    with open(r'D:\通讯录.csv','w+',newline='') as f :
        writer=csv.writer(f)
        writer.writerows(ldicTXL)
except IOError:
    print('写入文件失败')
else:
    print('通讯录生成成功')

#查找时：
#读取文件

readTXL={}
try:
    a=input('请输入姓名：')
    with open(r'D:\通讯录.csv','r',newline='') as f :
        reader=csv.reader(f)
        for i in reader:
            readTXL[i[0]]=[i[j] for j in range(1,len(i))]#生成查找字典
    print(readTXL.get(a,'没有该同学的联系方式'))
except IOError:
    print('读取文件失败')




    
        
