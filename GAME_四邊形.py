# -*- coding: utf-8 -*-
"""
Created on Dec 2022
@author: Y.C
"""
'''計算斜率'''
from collections import Counter
def cal_slope(a,b):
    try:
        return round((abs(int(b[1])-int(a[1]))) / (abs(int(b[0])-int(a[0]))),4)
    except ZeroDivisionError:
        return 'X'
'''斜率判斷(三點貢獻問題、平行四邊形&梯形分辨)'''
def check_slope(x): #放new_pts
    slope_list=[]
    slope_list.append(cal_slope(x[1],x[0]))
    slope_list.append(cal_slope(x[2],x[1]))
    slope_list.append(cal_slope(x[3],x[2]))
    slope_list.append(cal_slope(x[0],x[3]))
    slope_list.append(cal_slope(x[1],x[3]))
    slope_list.append(cal_slope(x[2],x[0]))
    return slope_list
#def quadrilateral():
co_list=[]
for i in range(1,5):
    each_co=[]
    while True:
        try:
            print("X",i,":",sep="",end=" ")
            each_co_x = int(input())
            print("Y",i,":",sep="",end=" ")
            each_co_y =int(input())
            each_co.append(each_co_x)
            each_co.append(each_co_y)
            co_list.append(each_co)
            break
        except:
            print("Input Error")
sorted(co_list)
LL=[] #Line_List

line_1 = (abs(co_list[0][0]-co_list[1][0])**2 + abs(co_list[0][1]-co_list[1][1])**2)**(1/2)
line_2 = (abs(co_list[1][0]-co_list[2][0])**2 + abs(co_list[1][1]-co_list[2][1])**2)**(1/2)
line_3 = (abs(co_list[2][0]-co_list[3][0])**2 + abs(co_list[2][1]-co_list[3][1])**2)**(1/2)
line_4 = (abs(co_list[3][0]-co_list[0][0])**2 + abs(co_list[3][1]-co_list[0][1])**2)**(1/2)
line_5 = (abs(co_list[1][0]-co_list[3][0])**2 + abs(co_list[1][1]-co_list[3][1])**2)**(1/2)
line_6 = (abs(co_list[0][0]-co_list[2][0])**2 + abs(co_list[0][1]-co_list[2][1])**2)**(1/2)

LL.append(round(line_1,6))
LL.append(round(line_2,6))
LL.append(round(line_3,6))
LL.append(round(line_4,6))
LL.append(round(line_5,6))
LL.append(round(line_6,6))

LL.sort()
for i in co_list:
    print("(",i[0],",",i[1],")",sep="",end=" ")
print()
if LL[0]==LL[1] and LL[1]==LL[2] and LL[2]==LL[3] and LL[0]==LL[3]:        
    if round(LL[0] * (2**(1/2)),6) == round(LL[5],6) : #1:1:2(1/2)
        print("正方形")
elif LL[1]==LL[2] and LL[2]==LL[3] and LL[3]==LL[4]:
    print("菱形(平行四邊形)")
elif (LL[0]==LL[1] and LL[2]==LL[3]) and (LL[4]==LL[5]) and (round((LL[0]**2 + LL[2]**2),6) == round(LL[5]**2),6): #長方形
    print("長方")
elif ((((LL[1]**2)-((LL[2]*0.5)**2))**(1/2))+(((LL[3]**2)-((LL[2]*0.5)**2))**(1/2)) ==LL[5] )or((((LL[1]**2)-((LL[0]*0.5)**2))**(1/2))+(((LL[3]**2)-((LL[0]*0.5)**2))**(1/2)) ==LL[5] ):
    print("箏型")    
elif (LL[0]==LL[1] or LL[1]==LL[2] ):
    print("平行四邊形or梯形")

else:
    print("不規則")

print("INTRO:\nWhat kind of quadrilateral can a Given list of four coordinates constitude")
#quadrilateral()




counterB=Counter(check_slope(co_list))
counterB.most_common(1)[0][1]
