import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import numpy
plt.rcParams['font.sans-serif']=['Kaiti']

Names=['曹操','司马懿','刘备','诸葛亮','孙权','周瑜','关羽','张飞','貂蝉','孙尚香',\
'大乔','小乔','黄忠','赵云','吕布','董卓','袁绍','袁术',\
'刘表','刘璋','马谡','马忠','黄盖','曹丕',\
'阿斗']
dic={}
with open(r'D:\三国演义.txt','r', encoding='utf8') as f:
    s=f.read().split('\n')
    f.close()
for pragra in s:
    for name1 in Names:
        if name1 in pragra:
            for name2 in Names:
                
                if name1==name2 or (name2,name1)in dic.keys():
                    continue
                elif name2 in pragra:

                    dic[(name1,name2)]=dic.get((name1,name2),0)+1
ldic=list(dic.items())
ldic.sort(key=lambda x: x[1],reverse=True)

net={}
maxnum=max([k[1] for k in ldic])

for i in ldic:
    net[i[0]]=i[1]/maxnum
#print(net)


matplotlib.rcParams['font.family']='Kaiti'
plt.figure(figsize=(15,15))
netg=nx.Graph()

for k,v in net.items():
    netg.add_edge(k[0],k[1],weight=v)
    #print(k[0],k[1])
#print(netg.nodes)
pos=nx.spring_layout(netg)
nx.draw_networkx_nodes(netg,pos,nodelist=netg,alpha=0.95,node_size=800)
nx.draw_networkx_edges(netg,pos,width=0.8)
nx.draw_networkx_labels(netg,pos,font_size=12)
plt.title("title")
plt.show()



    