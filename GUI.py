from tkinter import *
import os

from tkinter.ttk import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
import tkinter as tk
import matplotlib.animation as animation
import random
import json
import time
import ctypes
from random import random
import threading
import numpy as np
import matplotlib
matplotlib.use("TKAgg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from mpl_toolkits.mplot3d import Axes3D
from pylab import mpl
import datetime
import csv
import numpy as np
import pandas as pd

total_data = []

def __len__(self, *args, **kwargs): # real signature unknown
    """ Return len(self). """
    pass
def move_figure(f, x, y):
    """Move figure's upper left corner to pixel (x, y)"""
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    elif backend == 'WXAgg':
        f.canvas.manager.window.SetPosition((x, y))
    else:
        # This works for QT and GTK
        # You can also use window.setGeometry
        f.canvas.manager.window.move(x, y)

win = tk.Tk()
win.title("多通道生理数据获取系统")
win.geometry('550x300+600+250')

# 不可调整
win.resizable(0, 0)

#8个复选框
monty2 = ttk.LabelFrame(win, text='通道选择区')
monty2.grid(column=0, row=0, padx=20, pady=10)

var1 = tk.IntVar()
check1 = tk.Checkbutton(monty2, text="通道一",bg="#4A4A4A",font=('Song', 13),onvalue =1,offvalue = 0 ,variable=var1) # ,font=('Song', 13)
check1.select() # Clears (turns off) the checkbutton.
check1.grid(column=0, row=0,  padx = 10,pady=15)

var2 = tk.IntVar()
check2 = tk.Checkbutton(monty2, text="通道二", bg="#4A4A4A",font=('Song', 13),onvalue =1,offvalue = 0,variable=var2)
check2.select() # Clears (turns off) the checkbutton.
check2.grid(column=0, row=1,  padx = 10,pady=15)


var3 = tk.IntVar()
check3 = tk.Checkbutton(monty2, text="通道三",bg="#4A4A4A",font=('Song', 13),onvalue =1,offvalue = 0 ,variable=var3)
check3.select() # Clears (turns off) the checkbutton.
check3.grid(column=0, row=2,  padx = 10,pady=15)


var4 = tk.IntVar()
check4 = tk.Checkbutton(monty2, text="通道四",bg="#4A4A4A",font=('Song', 13), onvalue =1,offvalue = 0 ,variable=var4)
check4.select()  # Clears (turns off) the checkbutton.
check4.grid(column=0, row=3,  padx = 10,pady=15)

var5 = tk.IntVar()
check5 = tk.Checkbutton(monty2, text="通道五",bg="#4A4A4A",font=('Song', 13), onvalue =1,offvalue = 0 ,variable=var5)
check5.select() # Clears (turns off) the checkbutton.
check5.grid(column=1, row=0, padx = 10,pady=15)

var6 = tk.IntVar()
check6 = tk.Checkbutton(monty2, text="通道六",bg="#4A4A4A",font=('Song', 13), onvalue =1,offvalue = 0 ,variable=var6)
check6.select()# Clears (turns off) the checkbutton.
check6.grid(column=1, row=1, padx = 10,pady=15)


var7 = tk.IntVar()
check7 = tk.Checkbutton(monty2, text="通道七",bg="#4A4A4A",font=('Song', 13), onvalue =1,offvalue = 0 ,variable=var7)
check7.select() # Clears (turns off) the checkbutton.
check7.grid(column=1, row=2, padx = 10,pady=15)


var8= tk.IntVar()
check8 = tk.Checkbutton(monty2, text="通道八",bg="#4A4A4A",font=('Song', 13), variable=var8,onvalue =1,offvalue = 0)
check8.select()  # Clears (turns off) the checkbutton.
check8.grid(column=1, row=3, padx = 10,pady=15)



def ReturnAD():
    # 采集频率RF的含义是1S保存几个点。0.5HZ = 1秒0.5个点。或者说：2秒1个点
    # t秒保存一个次数值
    global total_data
    RF = int(e1.get())
   
    if total_data !=[]:
        tk.messagebox.showwarning(title="警告", message="历史数据未清空，请清空缓存后再试！")
    else:
        t = 1 / RF
        user_check=tk.messagebox.askyesno(title="提示",
                               message="-------------【通道开关情况】---------------\n\t一号通道开关情况:{}\n\t二号通道开关情况:{}\n\t三号通道开关情况:{}\n\t四号通道开关情况:{}\n"
              "\t五号通道开关情况:{}\n\t六号通道开关情况:{}\n\t七号通道开关情况:{}\n\t八号通道开关情况:{}\n----------------------------------------------\n     【是否进入电压监测动图绘制界面？】".format(var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get()))
        if user_check: # 检测开关情况
         # 暂停的秒数，t秒保存一个次数值
            # plt.rcParams['font.sans-serif'] = ['Song']
            plt.rcParams['axes.unicode_minus'] = False

            interval = t * 1000
            x_len = 5000  # Number of points to display
            y_range = [-500,500]
            y_ticks = [i for i in range(-200,201,20)]  # Range of possible Y values to display
            # Create figure for plotting
            fig1 = plt.figure(figsize=(14,7),dpi=130)
            ax1 = fig1.add_subplot(4, 2, 1)
            ax2 = fig1.add_subplot(4, 2, 2)
            ax3 = fig1.add_subplot(4, 2, 3)
            ax4 = fig1.add_subplot(4, 2, 4)
            ax5 = fig1.add_subplot(4, 2, 5)
            ax6 = fig1.add_subplot(4, 2, 6)
            ax7 = fig1.add_subplot(4, 2, 7)
            ax8 = fig1.add_subplot(4, 2, 8)
            xs = list(range(0, 5000))
            ys1 = [0] * x_len
            ys2 = [0] * x_len
            ys3 = [0] * x_len
            ys4 = [0] * x_len
            ys5 = [0] * x_len
            ys6 = [0] * x_len
            ys7 = [0] * x_len
            ys8 = [0] * x_len

            ax1.set_ylim(y_range)
            ax2.set_ylim(y_range)
            ax3.set_ylim(y_range)
            ax4.set_ylim(y_range)
            ax5.set_ylim(y_range)
            ax6.set_ylim(y_range)
            ax7.set_ylim(y_range)
            ax8.set_ylim(y_range)
            # Initialize communication with TMP102
            # tmp102.init()

            # Create a blank line. We will update the line in animate
            line1, = ax1.plot(xs, ys1,color ='plum',linewidth = 1)
            line2, = ax2.plot(xs, ys2,color ='red',linewidth = 1)
            line3, = ax3.plot(xs, ys3, color='darkcyan', linewidth=1)
            line4, = ax4.plot(xs, ys4, color='black', linewidth=1)
            line5, = ax5.plot(xs, ys5, color='green', linewidth=1)
            line6, = ax6.plot(xs, ys6, color='yellow', linewidth=1)
            line7, = ax7.plot(xs, ys7, color='m', linewidth=1)
            line8, = ax8.plot(xs, ys8, color='c', linewidth=1)
            # Add labels
            plt.sca(ax1)
            plt.title('通道1电信号监测图')
            plt.xlabel('时间(s)')
            plt.ylabel('电压(mV)')

            plt.sca(ax2)
            plt.title('通道2电信号监测图')
            plt.xlabel('时间(s)')
            plt.ylabel('电压(mV)')

            plt.sca(ax3)
            plt.title('通道3电信号监测图')
            plt.xlabel('时间(s)')
            plt.ylabel('电压(mV)')

            plt.sca(ax4)
            plt.title('通道4电信号监测图')
            plt.xlabel('时间(s)')
            plt.ylabel('电压(mV)')

            plt.sca(ax5)
            plt.title('通道5电信号监测图')
            plt.xlabel('时间(s)')
            plt.ylabel('电压(mV)')

            plt.sca(ax6)
            plt.title('通道6电信号监测图')
            plt.xlabel('时间(s)')
            plt.ylabel('电压(mV)')

            plt.sca(ax7)
            plt.title('通道7电信号监测图')
            plt.xlabel('时间(s)')
            plt.ylabel('电压(mV)')

            plt.sca(ax8)
            plt.title('通道8电信号监测图')
            plt.xlabel('时间(s)')
            plt.ylabel('电压(mV)')

            dates=[]    
            save_1,save_2,save_3,save_4,save_5,save_6,save_7,save_8, = [],[],[],[],[],[],[],[]

            def animate1(i, ys1):
                # Read temperature (Celsius) from TMP102
                # temp_c = round(tmp102.read_temp(), 2)
                temp_c1 = round(random() * 50, 2)
                date1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                # Add y to list
                dates.append(date1)
                ys1.append(temp_c1)
                save_1.append(temp_c1)
                # Limit y list to set number of items
                ysn1 = ys1[-x_len:]
                # Update line with new Y values
                line1.set_ydata(ysn1)
                return line1,

            def animate2(i, ys2):
                # Read temperature (Celsius) from TMP102
                # temp_c = round(tmp102.read_temp(), 2)
                temp_c2 = round(random() * -50, 2)
                save_2.append(temp_c2)
                # Add y to list
                ys2.append(temp_c2)
                # Limit y list to set number of items
                ysn2 = ys2[-x_len:]
                # Update line with new Y values
                line2.set_ydata(ysn2)
                return line2,

            def animate3(i, ys3):
                # Read temperature (Celsius) from TMP102
                # temp_c = round(tmp102.read_temp(), 2)
                temp_c3 = round(random() * 100, 2)
                save_3.append(temp_c3)
                ys3.append(temp_c3)
                # Limit y list to set number of items
                ysn3 = ys3[-x_len:]
                # Update line with new Y values
                line3.set_ydata(ysn3)
                return line3,

            def animate4(i, ys4):
                # Read temperature (Celsius) from TMP102
                # temp_c = round(tmp102.read_temp(), 2)
                temp_c4 = round(random() * -100, 2)
                save_4.append(temp_c4)
                # Add y to list
                ys4.append(temp_c4)
                # Limit y list to set number of items
                ysn4 = ys4[-x_len:]
                # Update line with new Y values
                line4.set_ydata(ysn4)
                return line4,

            def animate5(i, ys5):
                # Read temperature (Celsius) from TMP102
                # temp_c = round(tmp102.read_temp(), 2)
                temp_c5 = round(random() * 150, 2)
                save_5.append(temp_c5)
                # Add y to list
                ys5.append(temp_c5)
                # Limit y list to set number of items
                ysn5 = ys5[-x_len:]
                # Update line with new Y values
                line5.set_ydata(ysn5)
                return line5,


            def animate6(i, ys6):
                # Read temperature (Celsius) from TMP102
                # temp_c = round(tmp102.read_temp(), 2)
                temp_c6 = round(random() * -150, 2)
                save_6.append(temp_c6)
                # Add y to list
                ys6.append(temp_c6)
                # Limit y list to set number of items
                ysn6 = ys6[-x_len:]
                # Update line with new Y values
                line6.set_ydata(ysn6)
                return line6,

            def animate7(i, ys7):
                # Read temperature (Celsius) from TMP102
                # temp_c = round(tmp102.read_temp(), 2)
                temp_c7 = round(random() * 200, 2)
                save_7.append(temp_c7)
                # Add y to list
                ys7.append(temp_c7)
                # Limit y list to set number of items
                ysn7 = ys7[-x_len:]
                # Update line with new Y values
                line7.set_ydata(ysn7)
                return line7,

            def animate8(i, ys8):
                # Read temperature (Celsius) from TMP102
                # temp_c = round(tmp102.read_temp(), 2)
                temp_c8 = round(random() * -200, 2)
                save_8.append(temp_c8)
                # Add y to list
                ys8.append(temp_c8)
                # Limit y list to set number of items
                ysn8 = ys8[-x_len:]
                # Update line with new Y values
                line8.set_ydata(ysn8)
                return line8,

            #1-8通道同时打开结果
            if var1.get()==1 and var2.get()==1 and var3.get()==1 and var4.get()==1 and\
                    var5.get()==1 and var6.get()==1 and var7.get()==1 and var8.get()==1:
            # This function is called periodically from FuncAnimation

                #1通道绘制结果
                ani1 = animation.FuncAnimation(fig1,
                                              animate1,
                                              fargs=(ys1,),
                                              interval=interval,
                                              blit=True)
                # 2通道绘制结果
                ani2 = animation.FuncAnimation(fig1,
                                               animate2,
                                               fargs=(ys2,),
                                               interval=interval,
                                               blit=True)
                # 3通道绘制结果
                ani3 = animation.FuncAnimation(fig1,
                                               animate3,
                                               fargs=(ys3,),
                                               interval=interval,
                                               blit=True)
                #4 通道绘制结果
                ani4 = animation.FuncAnimation(fig1,
                                               animate4,
                                               fargs=(ys4,),
                                               interval=interval,
                                               blit=True)
                # 5通道绘制结果
                ani5 = animation.FuncAnimation(fig1,
                                               animate5,
                                               fargs=(ys5,),
                                               interval=interval,
                                               blit=True)
                # 6通道绘制结果
                ani6 = animation.FuncAnimation(fig1,
                                               animate6,
                                               fargs=(ys6,),
                                               interval=interval,
                                               blit=True)
                # 7通道绘制结果
                ani7 = animation.FuncAnimation(fig1,
                                               animate7,
                                               fargs=(ys7,),
                                               interval=interval,
                                               blit=True)
                #8通道绘制结果
                ani8 = animation.FuncAnimation(fig1,
                                               animate8,
                                               fargs=(ys8,),
                                               interval=interval,
                                               blit=True)

            # ***********单独通道2的数据传输************
            elif var2.get()==1:

                ani2 = animation.FuncAnimation(fig1,
                                              animate2,
                                              fargs=(ys2,),
                                              interval=interval,
                                              blit=True)

            # ***********通道3的数据传输************
            elif var3.get()==1:
                ani3 = animation.FuncAnimation(fig1,
                                              animate3,
                                              fargs=(ys3,),
                                              interval=interval,
                                              blit=True)

            # ***********通道3的数据传输************
            elif var4.get()==1:

                ani4 = animation.FuncAnimation(fig1,
                                              animate4,
                                              fargs=(ys4,),
                                              interval=interval,
                                              blit=True)

            #********************通道5*******************
            elif var5.get()==1:

                ani5 = animation.FuncAnimation(fig1,
                                              animate5,
                                              fargs=(ys5,),
                                              interval=interval,
                                              blit=True)

            # ************通道6数据******************
            elif var6.get()==1 and var7.get()==1:

                ani6 = animation.FuncAnimation(fig1,
                                              animate6,
                                              fargs=(ys6,),
                                              interval=interval,
                                              blit=True)
                ani7 = animation.FuncAnimation(fig1,
                                              animate7,
                                              fargs=(ys7,),
                                              interval=interval,
                                              blit=True)
                time.sleep(t)
            # ************通道7数据******************
            elif var7.get()==1:

                ani7 = animation.FuncAnimation(fig1,
                                              animate7,
                                              fargs=(ys7,),
                                              interval=interval,
                                              blit=True)

            #************通道8数据******************
            elif int(var8.get())==1:

                ani8 = animation.FuncAnimation(fig1,
                                              animate8,
                                              fargs=(ys8,),
                                              interval=interval,
                                              blit=True)

            plt.tight_layout()
            move_figure(fig1, 50, 30)
            plt.show()
            # print("电压监测展示完毕，请保存数据!")
            # print("时间列表:\n{}\n一号通道数据:\n{}\n二号通道数据:\n{}\n三号通道数据:\n{}\n四号通道数据:\n{}\n"
            #        "五号通道数据:\n{}\n六号通道数据:\n{}\n七号通道数据:\n{}\n八号通道数据:\n{}\n".format(dates,save_1,save_2,save_3,save_4,save_5,save_6,save_7,save_8))
            start_time = datetime.datetime.strptime(dates[0],'%Y-%m-%d %H:%M:%S')
            end_time = datetime.datetime.strptime(dates[-1],'%Y-%m-%d %H:%M:%S')
            seconds1 =  (start_time - end_time).seconds
            tk.messagebox.showinfo(title="提示",message="您开始采集的时间：{}\n您结束采集的时间：{}\n请您及时保存数据!".format(
                                   start_time, end_time))
            total_data.append(dates)
            if save_1:
                total_data.append(save_1)
            else:
                save_1 = [0]*len(dates)
                total_data.append(save_1)
            if save_2:
                total_data.append(save_2)
            else:
                save_2 = [0] * len(dates)
                total_data.append(save_2)
            if save_3:
                total_data.append(save_3)
            else:
                save_3 = [0] * len(dates)
                total_data.append(save_3)
            if save_4:
                total_data.append(save_4)
            else:
                save_4 = [0] * len(dates)
                total_data.append(save_4)
            if save_5:
                total_data.append(save_5)
            else:
                save_5 = [0] * len(dates)
                total_data.append(save_5)
            if save_6:
                total_data.append(save_6)
            else:
                save_6 = [0] * len(dates)
                total_data.append(save_6)
            if save_7:
                total_data.append(save_7)
            else:
                save_7 = [0] * len(dates)
                total_data.append(save_7)
            if save_8:
                total_data.append(save_8)
            else:
                save_8 = [0] * len(dates)
                total_data.append(save_8)
            return total_data
        else:
            pass




def save_data():
    header = ['监测时间', '通道一电压(mV)', '通道二电压(mV)', '通道三电压(mV)', '通道四电压(mV)', '通道五电压(mV)', '通道六电压(mV)', '通道七电压(mV)', '通道八电压(mV)']
    td = pd.DataFrame(total_data,index = header,).T
    try:
        td.to_csv("data.csv",encoding="utf_8_sig")
    except PermissionError:
        tk.messagebox.showwarning(title="警告", message="文件已经打开，请您关闭后重试")
    except:
        print("Error: you must enter two string")
        tk.messagebox.showwarning(title="警告", message="前期数据未清空，导致数据保存失败，请清空缓存后重新采集")
    else:
        tk.messagebox.showinfo(title="提示", message="数据保存成功！")



def flash():
    total_data.clear()
    if total_data:
        pass
    else:
        tk.messagebox.showinfo(title="提示", message="缓存清理成功！")


#####################################3第二个区域******************************
monty1 = ttk.LabelFrame(win,text = "功能区")
monty1.grid(column=1, row=0, padx=10, pady=10)

L3=tk.Label(monty1,text = "采集频率:", font = ('Song',13))
L3.grid(column=0, row=0, sticky='e', padx = 30,pady=10,)
tk.Label(monty1, width=15, height=3)

#文本输入框
vare1 = tk.StringVar()
e1 = tk.Entry(monty1,textvariable=vare1, bg="#DCDCDC",font=('Song', 11),highlightcolor='#76EEC6', highlightthickness=1)
e1.grid(column=1, row=0, padx = 5,pady=10,ipady=5,sticky = "w")

#三个按钮
b1 = tk.Button(monty1, text='开始采集', font=('Song', '15'),width=15, height=1, command=ReturnAD)
b1.grid(column=0, row=1, sticky='nesw', padx = 10,pady=12,columnspan = 2,rowspan = 1)

b2 = tk.Button(monty1, text='保存数据', 
                                 bg = "blue",
                                 fg = "red", font=('Song', '15'),width=15, height=1, command=save_data)
b2.grid(column=0,row=2,sticky='nesw', padx = 10,pady=12, columnspan = 2)


b3 = tk.Button(monty1, text='清空缓存', font=('Song', '15'),width=9, height=1, command=flash)
b3.grid(column=0, row=3, sticky='nesw', padx = 30,pady=10,columnspan = 2,rowspan = 1)



win.mainloop()