# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:35:38 2022

@author: Y.C
"""
def inputjudge(x):
    try:
        x = int(x)
        if x>3 or x<1:
            x=0
        
    except ValueError:
        x=0
    return x

def gameA():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    
    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
    
    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
       
    #1剪刀2石頭3布
    import random
    lista=[scissors,rock,paper]
    
    
    while True:#再來一次
        player_wintimes = 0 
        com_wintimes = 0
        while True: #三戰兩勝
            #print("第",max(player_wintimes,com_wintimes)+1,"局")
            while True:#每一局
                oppo = random.randint(1,3)
                oppofig=lista[oppo-1]
                
                while True: #出拳判斷
                    player = input("出拳-[1.剪刀 2.石頭 3.布 ]-\n")
                    judgeresult = int(inputjudge(player))
                    if judgeresult ==0:
                        print("輸入錯誤")
                    else:
                        break
                player = judgeresult
           
                playerfig = lista[player-1]
         
                result = oppo-player
                if result ==1 or result== -2:
                    print("玩家出:",playerfig)
                    print("電腦出:",oppofig)
                    print("L O S E")
                    com_wintimes+=1
                    break
                elif result ==0:
                    print("平手")
                else:
                    print("玩家出:",playerfig)
                    print("電腦出:",oppofig) 
                    print("W I N")
                    player_wintimes+=1
                    break
                
            print("玩家：",player_wintimes,"；電腦：",com_wintimes)    
            if player_wintimes ==2 or com_wintimes == 2:
                if player_wintimes ==2:
                    print("玩家獲勝")
                    break
                else:
                    print("電腦獲勝")
                    break        
            
        again = input("再一次? (y/n)")
        if again.lower() == "y":
            continue
        else:
            break
    
    
gameA()   












