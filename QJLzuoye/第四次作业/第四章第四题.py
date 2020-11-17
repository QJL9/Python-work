a=input('请输入字符串：')
l=a.split()
b=0
for i in l:
    if len(i)>b:
        b=len(i)

print(b)
    