import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import tkinter as tk
from tkinter import ttk

data3=pd.read_excel('house_unit_price.xlsx')
data4=data3[["LotShape","unitPrice"]]
group = data4.groupby('LotShape')

avg = group.mean('unitPrice')
avg2 = avg.sort_values(by = ["unitPrice"],ascending=True)
print(avg2)

matplotlib.rcParams['font.family']='SimHei'

avg2.plot(kind = 'bar', title='Bar graph',color='b')

plt.legend()
plt.savefig('./houseshape_unit_price.png',dpi=300)
plt.show()
