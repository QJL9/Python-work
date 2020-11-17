dicTXL={"小新":[13913000001,18191220001],"小亮":[13913000002,18191220002],"小刚":[13913000003,18191220003]}
dicother={"大刘":[13914000001,18191230001],"大王":[13914000002,181191230002],"大张":[13914000003,181191230003]}
dicTXL.update(dicother)
print(dicTXL)
dicWX={"小新":'xx9907',"小刚":'gang1004',"大王":'jack_w',"大刘":'liu666'}

for i in dicWX.keys():
    dicTXL[i]=[dicTXL[i][0],dicTXL[i][0],dicWX[i]]
print(dicTXL)
dicTXL["大王"][0]=13914000004
print(dicTXL)

a=input("请输入姓名：")
l=dicTXL.get(a,"没有该同学的联系方式")
print(l)