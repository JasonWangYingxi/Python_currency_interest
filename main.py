# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
import urllib.request
from tkinter import *
import tkinter as tk
from bs4 import BeautifulSoup
import datetime


class MainWindow(tk.Tk):
    def __init__(self, *args, **kw):
        super().__init__()
        self.title("Currency-refresh every minute")
        self.geometry("400x300+100+100")
        self.frame = tk.Frame(self)
        self.frame.pack()
        self.frame_c = tk.Frame(self.frame)
        self.frame_l = tk.Frame(self.frame)  # 第二层frame，左frame，长在主frame上
        self.frame_r = tk.Frame(self.frame)  # 第二层frame，右frame，长在主frame上
        self.frame_c.pack(side='top')
        self.frame_l.pack(side='left')
        self.frame_r.pack(side='right')
        self.label0 = tk.Label(self.frame_c, text=datetime.datetime.now(), bg='grey', font=('微软雅黑', 15)).grid(row=0)
        self.label1 = tk.Label(self.frame_l, text='✬货币名称:', font=('微软雅黑', 12)).grid(row=1, column=1)
        self.label2 = tk.Label(self.frame_l, text='✬现汇买入价:', font=('微软雅黑', 12)).grid(row=2, column=1)
        self.label3 = tk.Label(self.frame_l, text='✬现钞买入价:', font=('微软雅黑', 12)).grid(row=3, column=1)
        self.label4 = tk.Label(self.frame_l, text='✬现汇卖出价:', font=('微软雅黑', 12)).grid(row=4, column=1)
        self.label5 = tk.Label(self.frame_l, text='✬现钞卖出价:', font=('微软雅黑', 12)).grid(row=5, column=1)
        self.label6 = tk.Label(self.frame_l, text='✬中行折算价:', font=('微软雅黑', 12)).grid(row=6, column=1)
        self.label7 = tk.Label(self.frame_l, text='✬发布日期:', font=('微软雅黑', 12)).grid(row=7, column=1)
        self.label8 = tk.Label(self.frame_l, text='✬发布时间:', font=('微软雅黑', 12)).grid(row=8, column=1)
        self.label9 = tk.Label(self.frame_r, text='', bg='yellow', font=('微软雅黑', 12)).grid(row=1, column=2)
        self.label10 = tk.Label(self.frame_r, text='', bg='yellow', font=('微软雅黑', 12)).grid(row=2, column=2)
        self.label11 = tk.Label(self.frame_r, text='', bg='yellow', font=('微软雅黑', 12)).grid(row=3, column=2)
        self.label12 = tk.Label(self.frame_r, text='', bg='yellow', font=('微软雅黑', 12)).grid(row=4, column=2)
        self.label13 = tk.Label(self.frame_r, text='', bg='yellow', font=('微软雅黑', 12)).grid(row=5, column=2)
        self.label14 = tk.Label(self.frame_r, text='', bg='yellow', font=('微软雅黑', 12)).grid(row=6, column=2)
        self.label15 = tk.Label(self.frame_r, text='', bg='yellow', font=('微软雅黑', 12)).grid(row=7, column=2)
        self.label16 = tk.Label(self.frame_r, text='', bg='yellow', font=('微软雅黑', 12)).grid(row=8, column=2)
        self.after(60000, self.currency_display)
        self.mainloop()

    def currency_display(self):
        #print("i am refreshing")
        currency = self.rmbtousa()
        #print(currency)
        self.label0 = Label(self.frame_c, text=datetime.datetime.now(), bg='grey', font=('微软雅黑', 15)).grid(row=0)
        self.label1 = tk.Label(self.frame_l, text='✬货币名称:', font=('微软雅黑', 12)).grid(row=1, column=1)
        self.label2 = tk.Label(self.frame_l, text='✬现汇买入价:', font=('微软雅黑', 12)).grid(row=2, column=1)
        self.label3 = tk.Label(self.frame_l, text='✬现钞买入价:', font=('微软雅黑', 12)).grid(row=3, column=1)
        self.label4 = tk.Label(self.frame_l, text='✬现汇卖出价:', font=('微软雅黑', 12)).grid(row=4, column=1)
        self.label5 = tk.Label(self.frame_l, text='✬现钞卖出价:', font=('微软雅黑', 12)).grid(row=5, column=1)
        self.label6 = tk.Label(self.frame_l, text='✬中行折算价:', font=('微软雅黑', 12)).grid(row=6, column=1)
        self.label7 = tk.Label(self.frame_l, text='✬发布日期:', font=('微软雅黑', 12)).grid(row=7, column=1)
        self.label8 = tk.Label(self.frame_l, text='✬发布时间:', font=('微软雅黑', 12)).grid(row=8, column=1)
        self.label9 = tk.Label(self.frame_r, text=currency[0], bg='yellow', font=('微软雅黑', 12)).grid(row=1, column=2)
        self.label10 = tk.Label(self.frame_r, text=currency[1], bg='yellow', font=('微软雅黑', 12)).grid(row=2, column=2)
        self.label11 = tk.Label(self.frame_r, text=currency[2], bg='yellow', font=('微软雅黑', 12)).grid(row=3, column=2)
        self.label12 = tk.Label(self.frame_r, text=currency[3], bg='yellow', font=('微软雅黑', 12)).grid(row=4, column=2)
        self.label13 = tk.Label(self.frame_r, text=currency[4], bg='yellow', font=('微软雅黑', 12)).grid(row=5, column=2)
        self.label14 = tk.Label(self.frame_r, text=currency[5], bg='yellow', font=('微软雅黑', 12)).grid(row=6, column=2)
        self.label15 = tk.Label(self.frame_r, text=currency[6], bg='yellow', font=('微软雅黑', 12)).grid(row=7, column=2)
        self.label16 = tk.Label(self.frame_r, text=currency[7], bg='yellow', font=('微软雅黑', 12)).grid(row=8, column=2)
        #titles = ['货币名称','现汇买入价','现钞买入价','现汇卖出价','现钞卖出价','中行折算价','发布日期','发布时间']
        self.after(60000, self.currency_display)

    def filter_tags(self,htmlstr):
        # 先过滤CDATA
        re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
        re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
        re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
        re_h = re.compile('</?\w+[^>]*>')  # HTML标签
        re_comment = re.compile('<!--[^>]*-->')  # HTML注释
        del_label = re.compile(r'<[^>]+>', re.S)
        s = re_cdata.sub('', htmlstr)  # 去掉CDATA
        s = re_script.sub('', s)  # 去掉SCRIPT
        s = re_style.sub('', s)  # 去掉style
        s = del_label.sub("",s)
        s = re_h.sub('', s)  # 去掉HTML 标签
        s = re_comment.sub('', s)  # 去掉HTML注释
        s = re.split('\s+',s)
        return s

    def rmbtousa(self):
        url = "https://www.boc.cn/sourcedb/whpj/index.html"
        req = urllib.request.Request(url)
        f = urllib.request.urlopen(req)
        htmla = f.read().decode("utf-8")
        soup = BeautifulSoup(htmla, 'html.parser')
        #c = soup.find_all('tr')
        #print(soup)
        d = str(soup.get_text())
        #print(d)
        results = self.filter_tags(d)
        #print(results)
        i = 0
        num = len(results)
        result1 = []
        result2 = []
        while i < num:
            if results[i] == '货币名称':
                result1.append(results[i])
                result1.append(results[i+1])
                result1.append(results[i+2])
                result1.append(results[i+3])
                result1.append(results[i+4])
                result1.append(results[i+5])
                result1.append(results[i+6])
                result1.append(results[i+7])
            if results[i] == '美元' and results[i+1] != '瑞士法郎':
                result2.append(results[i])
                result2.append(results[i+1])
                result2.append(results[i+2])
                result2.append(results[i+3])
                result2.append(results[i+4])
                result2.append(results[i+5])
                result2.append(results[i+6])
                result2.append(results[i+7])
            i = i+1
        #print(result1)
        #print(result2)
        return result2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MainWindow = MainWindow()
