a=eval(input("请输入年份："))

if a%4==0 or a%400==0:
    print("闰年")
else:
    print("不是闰年")