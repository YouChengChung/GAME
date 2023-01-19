"""
Created on Dec 2022
@author: Y.C
"""
import random
import numpy as np
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
import random

###建立使用者視窗
win = tk.Tk()#定義主視窗為win
win.title("Python Sudo")#改寫視窗標題
win.geometry("725x520")#改視窗大小
win.resizable(False,False)

def start():
    global anslist
    global count
    anslist = []
    num = [0,1,2,3,4,5,6,7,8,9]
    while len(anslist)<4:
        a=random.randint(1, 10)
        if a in num:
            anslist.append(a)
            num.remove(a)
    print(anslist)
    print(count)
    
    tk_label_response['text']="INTRODUCTION : \n Guess a four digit number (unduplicated)\nPress 'Start' to play"
    outputarea['text']=" "
    outputarea1['text']=" "
    
    #tk_label_response['text'] = anslist

def guess():
    global count
    A=0
    B=0
    numbers=True
    guesslist=[]
    guessnum = tk_entry.get()
    #tk_label_response['text']=""

    for i in guessnum:
        if not i.isdigit():
            numbers=False
            break
        guesslist.append(int(i))
    if numbers==True:
        seta = set(guesslist)
        if len(seta) !=len(guesslist) or len(guesslist)!=4:
            print("數字重複或長度錯誤(INPUT ERROR)")
            tk_label_response['text'] = "數字重複或長度錯誤(INPUT ERROR)"
        else:
            for i in range(0,len(anslist)):
                if int(guessnum[i]) in anslist:
                    if int(guessnum[i]) == anslist[i]:
                        A+=1
                    #print(guess[i])
                    else:
                        B+=1
            count+=1
            tk_label_response['text']="INTRODUCTION : \n Guess a four digit number (unduplicated)\nPress 'Start' to play"
            if count <=15:
                outputarea['text']+=(str(count)+"    "+guessnum+"    ")
            elif count<=30:
                outputarea1['text']+=(str(count)+"    "+guessnum+"    ")

        if A==4:
            tk_label_response['text'] = "正確答案"
        elif len(seta) == len(guesslist) and len(guesslist)==4:
            result = str(A)+"A"+str(B)+"B"
            #tk_label_response['text']+=(result+"\n")
            if count <=15:
                outputarea['text']+=(result+"\n")
            elif count<=30:
                outputarea1['text']+=(result+"\n")
            else:
                tk_label_response['text'] = "超過限制\n答案為："
                for k in anslist:
                    tk_label_response['text'] += str(k) 
    else:
        tk_label_response['text'] = "請輸入數字"

fontExample = tkFont.Font(family="Microsoft JhengHei", size=12, weight="bold")
tk_label_response = tk.Label(win,text = "INTRODUCTION : \n Guess a four digit number (unduplicated)\nPress 'Start' to play",relief="groove")
tk_label_response.config(bd = 1,fg = "#000000",bg="DimGray",height=4,width=50, font=fontExample, justify='center')
tk_label_response.place(x=10, y=10)

tk_button = tk.Button(text = 'Start',bg="DimGray",width=12,command=start)
tk_button.config(bd = 1, padx=10, pady=10,font=fontExample)
tk_button.place(x=550, y=20)

tk_entry = tk.Entry(relief="groove")
tk_entry.config(bd = 1,fg = "#000000",bg="DimGray",width=14, font=fontExample, justify='center')
tk_entry.place(x=550, y=150)
count=0
guess_button = tk.Button(text = 'GUESS',bg="Wheat",width=12,command=guess)
guess_button.config(bd = 1, padx=10, pady=10,font=fontExample)
guess_button.place(x=550, y=180)

outputarea = tk.Label(win,text="",relief="groove")
outputarea.config(bd = 1,fg = "#000000",bg="DimGray",height=18,width=24, font=fontExample, justify="right")
outputarea.place(x=10, y=100)
outputarea1= tk.Label(win,text="",relief="groove")
outputarea1.config(bd = 1,fg = "#000000",bg="DimGray",height=18,width=24, font=fontExample, justify="right")
outputarea1.place(x=270, y=100)

tk_botton2 = tk.Button(text = '結束',bg="Wheat",width=12,command=win.destroy)
tk_botton2.config(bd = 1, padx=10, pady=10,font=fontExample)
tk_botton2.place(x=550, y=400)

start()
win.mainloop()