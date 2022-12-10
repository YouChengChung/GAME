# -*- coding: utf-8 -*-
"""
Created on Dec 2022
@author: Y.C
"""
def quadrilateral():
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

    LL.append(line_1)
    LL.append(line_2)
    LL.append(line_3)
    LL.append(line_4)
    LL.append(line_5)
    LL.append(line_6)

    LL.sort()
    for i in co_list:
        print("(",i[0],",",i[1],")",sep="",end=" ")
    print()
    if LL[0]==LL[1] and LL[1]==LL[2] and LL[2]==LL[3] and LL[0]==LL[3]:        
        if LL[0] * (2**(1/2)) == LL[5] : #1:1:2(1/2)
            print("正方形")
        else:
            print("菱形")
    elif (LL[0]==LL[1] and LL[2]==LL[3]) and (LL[4]==LL[5]) and ((LL[0]**2 + LL[2]**2) == LL[5]**2): #長方形
        print("長方形")
    elif (LL[0]==LL[1] or LL[1]==LL[2] )and LL[3]==LL[4] :
        print("平行四邊形")
    elif LL[0]==LL[1] and LL[2]==LL[3]:
        print("箏形")
    else:
        print("不規則")

print("INTRO:\nWhat kind of quadrilateral can a Given list of four coordinates constitude")
quadrilateral()
