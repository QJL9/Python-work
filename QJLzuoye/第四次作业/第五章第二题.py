
l={'012':[90,94,97,86,85,89,88,85],'005':[91,91,92,98,90,96,90,95],\
    '108':[96,86,97,96,87,86,86,96],'037':[95,95,94,93,97,98,99,95],\
    '066':[95,87,94,94,93,99,96,97],'020':[89,97,91,95,89,94,97,92]}
lavg={}
for k in l.keys():
    maxx=max(l[k])
    minn=min(l[k])
    total=sum(l[k])
    lavg[k]=round((total-maxx-minn)/6,2)
print(lavg)

print(sorted(lavg.items(),key=lambda x:x[1],reverse=True))


#llavg=[ (v,k) for k,v in lavg.items()]
#llavg.sort(reverse=True)
#llavg=[ (v,k) for k,v in llavg]
#print(llavg)


    
