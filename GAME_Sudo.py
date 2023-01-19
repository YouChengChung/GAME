'''SUDO'''
import random
import numpy as np
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont

# 以現有數獨創造新的數獨矩陣(模擬魔術方塊轉動)
def random_sudo(sudo, times):
    ranlist=[0,3,6]
    for _ in range(times):
        # 隨機交換兩行
        rand_row_base = random.sample(ranlist, 1)  ##隨機取任一個3*3小九宮格(0,3,6分別代表從左數來第1,,3個3*3小九宮格
        rand_rows = random.sample(range(3), 2)   ##從小九宮格中取任意兩行
        row_1 = rand_row_base[0] + rand_rows[0]
        row_2 = rand_row_base[0] + rand_rows[1]
        sudo[[row_1, row_2], :] = sudo[[row_2, row_1], :]
    
        # 隨機交換兩列
        rand_col_base = random.sample(ranlist, 1)
        rand_cols = random.sample(range(3), 2)
        col_1 = rand_col_base[0] + rand_cols[0]
        col_2 = rand_col_base[0] + rand_cols[1]
        sudo[:, [col_1, col_2]] = sudo[:, [col_2, col_1]]
           
        #小九宮格互換:列交換
        rand_block_base = random.sample(ranlist, 2)
        block_1 = [rand_block_base[0] ,rand_block_base[0]+1,rand_block_base[0]+2]
        block_2 = [rand_block_base[1] ,rand_block_base[1]+1,rand_block_base[1]+2]
        sudo[block_1+block_2,:] = sudo[block_2+block_1,:]
           
        #小九宮格互換:行交換
        rand_block_base = random.sample(ranlist, 2)
        block_1 = [rand_block_base[0] ,rand_block_base[0]+1,rand_block_base[0]+2]
        block_2 = [rand_block_base[1] ,rand_block_base[1]+1,rand_block_base[1]+2]
        sudo[:,block_1+block_2] = sudo[:,block_2+block_1]

###清除隨機空格
def get_sudo_subject(sudo, del_nums):
    subject = sudo.copy()
    # 依照級別清除不同數量數字
    #初級清除15、中級44、高級55、困難59
    clears = random.sample(range(81), del_nums)
    for clear_index in clears:
        # 0-80轉換為行列索引
        row_index = clear_index // 9
        col_index = clear_index % 9
        subject[row_index, col_index] = 0
    return subject        

###創造基礎數獨矩陣
board=[[5, 2, 7, 8, 9, 3, 6, 4, 1],\
        [9, 3, 4, 6, 1, 2, 5, 7, 8],\
        [6, 1, 8, 5, 7, 4, 2, 3, 9],\
        [2, 4, 6, 9, 3, 8, 1, 5, 7],\
        [1, 9, 3, 2, 5, 7, 8, 6, 4],\
        [8, 7, 5, 1, 4, 6, 9, 2, 3],\
        [3, 5, 2, 7, 8, 1, 4, 9, 6],\
        [7, 8, 9, 4, 6, 5, 3, 1, 2],\
        [4, 6, 1, 3, 2, 9, 7, 8, 5]]
def create_sudo():
    global sudo
    global sudo_subj
    sudo = np.array(board) #答案
    #創造新的數獨
    random_sudo(sudo,50)
    if level == 0:
        sudo_degree = 81
    if level == 1 :
        sudo_degree=15  #空格數量
    elif level == 2:
        sudo_degree=40
    elif level == 3:
        sudo_degree=53
    
    sudo_subj = get_sudo_subject(sudo,sudo_degree) #問題

###建立使用者視窗
win = tk.Tk()#定義主視窗為win
win.title("Python Sudo")#改寫視窗標題
win.geometry("725x520")#改視窗大小
win.resizable(False,False)
win.config(bg='#fef4a9')

#格線(一格50,邊界10)
def draw_boundary():
    header = Frame(win, bg='Maroon', height=3,width=725)
    header.place(x=0, y=0)
    boundTop = Frame(win, bg='DarkSlateGray', height=4,width=450)
    boundTop.place(x=45, y=45)
    boundBottom = Frame(win, bg='DarkSlateGray', height=4,width=450)
    boundBottom.place(x=45, y=491)
    boundLeft = Frame(win, bg='DarkSlateGray', height=445,width=4)
    boundLeft.place(x=45, y=49)
    boundRight = Frame(win, bg='DarkSlateGray', height=445,width=4)
    boundRight.place(x=491, y=49)

    horizontal  = Frame(win, bg='DarkSlateGray', height=4,width=450)
    horizontal.place(x=45, y=193)
    horizontal1 = Frame(win, bg='DarkSlateGray', height=4,width=450)
    horizontal1.place(x=45, y=343)
    vertical = Frame(win, bg='DarkSlateGray', height=442,width=4)
    vertical.place(x=193, y=49)
    vertical1 = Frame(win, bg='DarkSlateGray', height=442,width=4)
    vertical1.place(x=343, y=49)
draw_boundary()

#繪製界面
def restartbutton():
    create_sudo()
    global blank
    blank=[]#空格位置
    for i in range(9): #列
        for j in range(9): #欄
            if sudo_subj[i,j] != 0 :
                tk_label=tk.Label(win, text=sudo_subj[i,j], relief="flat")
                tk_label.config(bg = "SlateGray",fg = "#000000", bd=10,height=1,width=2, font=('Arial 12'), justify='center')
                tk_label.place(x= (i+1)*50,y= (j+1)*50)
            else :
                globals()['tk_entry'+str(j)+str(i)] = tk.Entry(relief="flat")
                #tk_entry = tk.Entry(relief="flat")
                globals()['tk_entry'+str(j)+str(i)].config(bg = "Tan",fg = "#000000", bd=10,width=2,font=('Arial 12'), justify='center')
                globals()['tk_entry'+str(j)+str(i)].place(x= (i+1)*50, y= (j+1)*50)
                blank.append([j,i])

#檢查答案
def text1():
    try:
        for k in blank:
            t = globals()['tk_entry'+str(k[0])+str(k[1])].get()
            #print(t)
            print(k[0],",",k[1],":",t) #行,列
            sudo_subj[k[1],k[0]] = t
        if np.array_equal(sudo,sudo_subj):
            result = "正確"
            print(result)
        else:
            result = "有錯"
            print(result)
    except ValueError:
        if level ==0:
            result = "先選擇難度"
        else:
            result = "還有空格沒填"
        print(result)
    tk_label_response['text'] = result
    #print(sudo_subj)
    #print(sudo)
#清除所有答案
def clearbutton():
    for k in blank:
        globals()['tk_entry'+str(k[0])+str(k[1])].delete(0,'end')
#難度等級 預設為0
level = 0
def getlevel():
    global level
    level =  radio.get()

fontExample = tkFont.Font(family="Microsoft JhengHei", size=12, weight="bold")
#RESPONSE BAR
tk_label_response = tk.Label(win,text = "",relief="groove")
tk_label_response.config(bd = 1,fg = "#000000",bg="LightCoral",height=2,width=19, font=fontExample, justify='center')
tk_label_response.place(x=500, y=170)
#BUTTONS
def BUTTONS():
    tk_botton = tk.Button(text = '提交',bg="Wheat",width=12,command=text1)
    tk_botton.config(bd = 1, padx=10, pady=10,font=fontExample)
    tk_botton.place(x=525, y=250)

    tk_botton1 = tk.Button(text = '清空',bg="Wheat",width=12,command=clearbutton)
    tk_botton1.config(bd = 1, padx=10, pady=10,font=fontExample)
    tk_botton1.place(x=525, y=325)

    tk_botton2 = tk.Button(text = '結束',bg="Wheat",width=12,command=win.destroy)
    tk_botton2.config(bd = 1, padx=10, pady=10,font=fontExample)
    tk_botton2.place(x=525, y=400)

    tk_botton3 = tk.Button(text = 'Start',bg="Wheat",command= restartbutton,width=6)
    tk_botton3.config(bd = 1, padx=10, pady=10,font=('times'))
    tk_botton3.place(x=510, y=68)
BUTTONS()

radio = IntVar()
levelbutton1 = tk.Radiobutton(win, text='簡單',bg="#faf4a9",variable=radio ,value=1,command=getlevel)
levelbutton1.configure(font=fontExample)
levelbutton1.place(x=600, y=45)
levelbutton2 = tk.Radiobutton(win, text='中等',bg="#faf4a9",variable=radio, value=2,command=getlevel)
levelbutton2.configure(font=fontExample)
levelbutton2.place(x=600, y=75)
levelbutton3 = tk.Radiobutton(win, text='困難',bg="#faf4a9",variable=radio, value=3,command=getlevel)
levelbutton3.place(x=600, y=105)
levelbutton3.configure(font=fontExample)


restartbutton()
win.mainloop()
