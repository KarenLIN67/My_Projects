from tkinter import *
import pandas as pd
import requests
import re
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def printSelection():
    year = []
    value = []
    
    url = urllist[var.get()]
    response = requests.get(url)
    m = re.search("(\[.*\])",response.text)

    str1 = m.group(1)

    #取出圖表中數值
    list_first = str1.split(",")
    value_connect = ":"
    value_str = value_connect.join(list_first)
    value_list = value_str.split(":")
    value_len = len(value_list)

    for k in range(value_len):
        if k % 6 == 1:
            year.append(value_list[k])
        if k % 6 == 3:
            value.append(value_list[k])
    
    count = int(len(year)/6)
    
    #圖表
    fig = plt.figure(figsize=(9,5),facecolor="gray")
    cv = Canvas(win)
    cv.place(x=50, y=250)
    plt.subplot(111)
    plt.clf()
    plt.title(citytitlelist[var.get()]+" Daily confirmed cases", fontproperties="SimHei", fontsize=16)
    
    plt.plot(year,value,'g')
    ax = plt.gca()
    
    ax.xaxis.set_major_locator(ticker.MultipleLocator(count))
    plt.yticks(np.linspace(0, len(value), 7),['0','5000','10000','15000','20000','25000','30000'])

    plt.grid()
    
    canvas = FigureCanvasTkAgg(fig, master=cv)
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    plt.ioff()


#取得網址
url_head = "https://covid-19.nchc.org.tw/amchartsSource/output/chartdiv_009_town_"
url_tail = ".min.js"
url_taipei = url_head + "台北市" + url_tail
url_newtaipei = url_head + "新北市" + url_tail
url_keelung = url_head + "基隆市" + url_tail
url_yilan = url_head + "宜蘭縣" + url_tail
url_taoyuan = url_head + "桃園市" + url_tail
url_hsinchucity= url_head + "新竹市" + url_tail
url_hsinchucounty = url_head + "新竹縣" + url_tail
url_miaoli = url_head + "苗栗縣" + url_tail
url_taichung = url_head + "台中市" + url_tail
url_changhua = url_head + "彰化縣" + url_tail
url_nantou = url_head + "南投縣" + url_tail
url_yunlin = url_head + "雲林縣" + url_tail
url_chiayicity = url_head + "嘉義市" + url_tail
url_chiayicounty = url_head + "嘉義縣" + url_tail
url_tainan = url_head + "台南市" + url_tail
url_kaohsiung = url_head + "高雄市" + url_tail
url_pingtung = url_head + "屏東縣" + url_tail
url_hualien = url_head + "花蓮縣" + url_tail
url_tiatung = url_head + "台東縣" + url_tail
url_penghu = url_head + "澎湖縣" + url_tail
url_lianjiang = url_head + "連江縣" + url_tail
url_kinmen = url_head + "金門縣" + url_tail
url_imported = url_head + "境外移入" + url_tail

#建立視窗
win=Tk()
win.config(bg="lightskyblue")
win.geometry("1000x800")
win.title("期末報告")
win.update()

label1 = Label(win, text="各城市Covid-19即時資訊" , pady=3 ,fg="sandybrown" 
               ,bg="forestgreen", font=("標楷體",25))
label1.place(x=300, y=10)

var = IntVar()
var.set(0)
citytitlelist = {0:"Taipei", 1:"Newtaipei", 2:"Keelung", 3:"Yilan", 4:"Taoyuan", 5:"Hsinchu City",
            6:"Hsinchu County", 7:"Miaoli", 8:"Taichung", 9:"Changhua", 10:"Nantou", 11:"Yunlin",
            12:"Chiayi City", 13:"Chiayi County", 14:"Tainan", 15:"Kaohsiung", 16:"Pingtung", 17:"Hualien",
            18:"Tiatung", 19:"Penghu", 20:"Lianjiang", 21:"Kinmen", 22:"Imported"}

citylist = {0:"台北市", 1:"新北市", 2:"基隆市", 3:"宜蘭縣", 4:"桃園市", 5:"新竹市",
                6:"新竹縣", 7:"苗栗縣", 8:"台中市", 9:"彰化縣", 10:"南投縣", 11:"雲林縣",
                12:"嘉義市", 13:"嘉義縣", 14:"台南市", 15:"高雄市", 16:"屏東縣", 17:"花蓮縣",
                18:"台東縣", 19:"澎湖縣", 20:"連江縣", 21:"金門縣", 22:"境外移入"}


urllist = {0:url_taipei, 1:url_newtaipei, 2:url_keelung, 3:url_yilan,
           4:url_taoyuan, 5:url_hsinchucity, 6:url_hsinchucounty, 7:url_miaoli,
           8:url_taichung, 9:url_changhua, 10:url_nantou, 11:url_yunlin,
           12:url_chiayicity, 13:url_chiayicounty, 14:url_tainan, 15:url_kaohsiung,
           16:url_pingtung, 17:url_hualien, 18:url_tiatung, 19:url_penghu,
           20:url_lianjiang, 21:url_kinmen, 22:url_imported}

for i in range(0,3):
    for j in range(0,8):
        n = i * 8 + j
        if(n < len(citylist)):
            city1 = citylist[n]
            rbtem = Radiobutton(win, text=city1, variable=var, value=n, command=printSelection)
            rbtem.place(x = j * 90 + 150 ,y = i * 40 + 70)
            if(n==0):
                rbtem.select()

win.mainloop()