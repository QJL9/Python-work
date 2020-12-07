import pandas as pd
excel = pd.read_excel('C:\Codes\py\QJLzuoye\第七次作业\score.xlsx',sheet_name=[0,1],header=0)
score = excel[0]
duty = excel[1]
print(score)
#

print(score[0:3])
#
count= score.count()
print(count['学号'])
#


# l=[0,0,0,0,0,0,0]
# for i in range(0,7):
#     for j in range(3,6):
#         l[i]+=(float(score.iat[i,j]))
# score['总分']=l
# print(score)

total = (score['语文']+score['数学']+score['英语'])
score['总分']=total

score=score.sort_values(by=['总分'],ascending=False)
print(score)
group=score.groupby('性别')
avg=group.mean()
print(avg)
print(f'男生平均分={avg.iat[0,4]},女生平均分={avg.iat[1,4]}')

manmax=0
womanmax=0
for i in range(0,6):
    if score.iat[i,2]=='男':
        if score.iat[i,6]>manmax:
            manmax=score.iat[i,6]

    elif score.iat[i,6]>womanmax:
        womanmax=score.iat[i,6]
print(f'男生最高分={manmax},女生最高分={womanmax}')



l2=[0,0,0,0,0,0,0]
for i in range(0,7):
    if score.iat[i,6]>=270:
        l2[i]='A'
    elif score.iat[i,6]>=210:
        l2[i]='B'
    else:
        l2[i]='C'
score['等级']=l2
print(score)

student = pd.merge(score,duty,how='left',on='学号')
print(student)

student.to_excel('C:\Codes\py\QJLzuoye\第七次作业\student.xlsx',sheet_name='sheet1')











