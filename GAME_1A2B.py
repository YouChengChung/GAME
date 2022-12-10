# -*- coding: utf-8 -*-
"""
Created on Dec 2022
@author: Y.C
"""
import random
def GAME():
    anslist = []
    num = [0,1,2,3,4,5,6,7,8,9]
    while len(anslist)<4:
        a=random.randint(1, 10)
        if a in num:
            anslist.append(a)
            num.remove(a)
    #print(anslist)
    A=0
    B=0
    T=0
    while A<4:
        T+=1
        A=0
        B=0
        guess = ''
        guesslist = []   
        while len(guess)!=4:
            guess = input("輸入相異四位數：(INPUT FOUR NUMBER)")       
            for i in guess:
                guesslist.append(int(i))
                #print(len(guess))
            seta = set(guesslist)
            if len(seta) !=4:
                print("數字重複或長度錯誤(IMPUT ERROR)")
                break
            for i in range(0,len(anslist)):
                if int(guess[i]) in anslist:
                    if int(guess[i]) == anslist[i]:
                        A+=1
                    #print(guess[i])
                    else:
                        B+=1
            if A==4:
                break
            #print("your guess:",guess)
            print(A,"A",B,"B")   
    print("正確答案！猜了",T,"次")

print("INTRO:\n1A2B is a puzzle game,player are asked to guess a four digit number (unduplicated)")
input("Press ENTER to continue")
while True:
    GAME()
    again = input("Want to play again?(y/n)")
    if again.upper() == "N":
        break
print("BYE!")
        
        




