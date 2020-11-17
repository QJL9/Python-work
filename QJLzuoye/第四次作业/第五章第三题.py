j1={"李雷","张玉","王晓刚","陈红静","方向","司马清"}
j2={"施然","李芳芳","刘潇","方向","孙一航","黄煌"}
j3={"陈红静","方向","刘培良","张玉","施小冉","司马清"}
count1=0
count2=0
count3=0
count4=0

for i in (j1|j2|j3):
    count1+=1
print(25-count1)

for i in j1&j2|j2&j3|j1&j3:
    count2+=1
print(count2)

for i in j1&j2&j3:
    count3+=1
print(count3)

for i in j1-j2-j3|j2-j1-j3|j3-j1-j2:
    count4+=1
print(count4)