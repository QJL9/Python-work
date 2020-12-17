import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.title("CourseDesign")

outputvar = tk.StringVar()

try:
    #functions
    def command1():
        global data,text
        try:
            inputfilenamevar = filedialog.askopenfilename(title='choose input file')
            if inputfilenamevar=='':
                return
            data = pd.read_csv(inputfilenamevar)
            data.dropna(axis=0, how='any')
            text.insert("end", data.head(5))
            text.insert("end", '\n')
            text.insert("end", data.tail(2))
            # print(data.head(5))
            # print(data.tail(2))
        except IOError:
            messagebox.showerror('Error!','文件读取出错，请检查输入路径')
            
        else:
            messagebox.showinfo(message='success!')



    def command2():
        
        outputfilename = filedialog.asksaveasfilename(title='choose output file')
        if outputfilename=='':
            return
        global data
        data1 = data[['Id','LotShape','LotArea','OverallCond',
                        'YrSold','SalePrice']]
        try:                
            data1.to_csv(outputfilename,sep=' ',index=0)
        except IOError:
            messagebox.showerror('Error!','文件输出出错')
            
        else:
            messagebox.showinfo(message='success!')
    # # with open('./house.sale.price.csv','w') as f:
    # #     for col in l1:
    # #         for i in data[col]:
    # #             f.write(str(i)+' ')
    # #         f.write('\n')

    def command3():
        inputfilenamevar = filedialog.askopenfilename(title='choose input file')
        if inputfilenamevar=='':
            return

        try:
            price=pd.read_csv(inputfilenamevar,sep=' ')
        except IOError:
            messagebox.showerror('Error!','文件读取出错，请检查输入路径')
        #
        #   另一种方法
        #   unitprice = (price['SalePrice']/price['LotArea'])
        #   price['unitPrice']=unitPrice
        #
        #
        unitPrice=[]
        for i in price['SalePrice']:
            for j in price['LotArea']:
                unitPrice.append(round(i/j,2))
                break
        price['unitPrice']=unitPrice
        
        outputfilename = filedialog.asksaveasfilename(title='choose output file')
        if outputfilename=='':
            return
        try:
            price.to_excel(outputfilename,index=0)
        except IOError:
            messagebox.showerror('Error!','文件输出出错')
        else:
            messagebox.showinfo(message='success!')

    def command4():
        inputfilenamevar = filedialog.askopenfilename(title='choose input file')
        if inputfilenamevar=='':
            return        
        outputfilename = filedialog.asksaveasfilename(title='choose output file')
        if outputfilename=='':
            return
        try:
            data3=pd.read_excel(inputfilenamevar)
        except IOError:
            messagebox.showerror('Error!','文件读取出错，请检查输入路径')

        data4=data3[["LotShape","unitPrice"]]
        group = data4.groupby('LotShape')

        avg = group.mean('unitPrice')
        avg2 = avg.sort_values(by = ["unitPrice"],ascending=True)
        #print(avg2)

        matplotlib.rcParams['font.family']='SimHei'

        avg2.plot(kind = 'bar', title='Bar graph',color='b')

        plt.legend("LotShap-unitPrice")
        try:
            plt.savefig(outputfilename,dpi=300)
            plt.show()
        except IOError:
            messagebox.showerror('Error!','文件输出出错')
        else:
            messagebox.showinfo(message='success!')
        


    def command5():
        inputfilenamevar = filedialog.askopenfilename(title='choose input file')
        if inputfilenamevar=='':
            return
        outputfilename = filedialog.asksaveasfilename(title='choose output file')
        if outputfilename=='':
            return
        
        try:
            data3=pd.read_excel(inputfilenamevar)
        except IOError:
            messagebox.showerror('Error!','文件读取出错，请检查输入路径')
        
        data4=data3[["LotShape","OverallCond"]]
        group = data4.groupby('LotShape')

        avg = group.mean('OverallCond')
        avg2 = avg.sort_values(by = ["OverallCond"],ascending=False)
        #print(avg2)

        matplotlib.rcParams['font.family']='SimHei'

        avg2.plot(kind = 'bar', title='Bar graph',color='b')

        plt.legend("LotShap-OverallCond")
        try:
            plt.savefig(outputfilename,dpi=300)
            #plt.show()
        except IOError:
            messagebox.showerror('Error!','文件输出出错')
        else:
            messagebox.showinfo(message='success!')
        
    #widgets

    fram = ttk.Frame(root,padding="10 10 10 5")

    label1 = ttk.Label(fram, text="func1")
    label2 = ttk.Label(fram, text="func2")
    label3 = ttk.Label(fram, text="func3")
    label4 = ttk.Label(fram, text="func4")
    label5 = ttk.Label(fram, text="func5")

    btn1 = ttk.Button(fram, text="func1", command=command1)
    btn2 = ttk.Button(fram, text="func2", command=command2)
    btn3 = ttk.Button(fram, text="func3", command=command3)
    btn4 = ttk.Button(fram, text="func4", command=command4)
    btn5 = ttk.Button(fram, text="func5", command=command5)

    # entry1 = ttk.Entry(fram, textvariable=evariable1, width=17)
    # entry2 = ttk.Entry(fram, textvariable=evariable2, width=17)
    # entry3 = ttk.Entry(fram, textvariable=evariable3, width=17)
    text = tk.Text(fram, width=50, height=10)

    fram.grid(row=0,column=0,sticky=(tk.N, tk.S, tk.E,tk.W))

    label1.grid(row=0,column=0)
    label2.grid(row=1,column=0)
    label3.grid(row=2,column=0)
    label4.grid(row=3,column=0)
    label5.grid(row=4,column=0)

    btn1.grid(row=0,column=1,pady=5)
    btn2.grid(row=1,column=1,pady=5)
    btn3.grid(row=2,column=1,pady=5)
    btn4.grid(row=3,column=1,pady=5)
    btn5.grid(row=4,column=1,pady=5)

    text.grid(row=5,column=0,columnspan=2,sticky=(tk.N, tk.S, tk.E,tk.W))

    fram.rowconfigure(0, weight=1)
    fram.rowconfigure(1, weight=1)
    fram.rowconfigure(2, weight=1)
    fram.rowconfigure(3, weight=1)
    fram.rowconfigure(4, weight=1)
    fram.rowconfigure(5, weight=3)
    fram.columnconfigure(0, weight=1)
    fram.columnconfigure(1, weight=1)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
except Exception as e:
    messagebox.showerror('Error!','e\ncontect QJL @qjl.cug.edu.cn')

root.mainloop()



