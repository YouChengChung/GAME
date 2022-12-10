import random
class GAME_GuessNumber:
    def guess_judge(self,x,a,b):        
        try:
            x=int(x)
            if x>a and x<b:
                return x
            else:
                print("超出範圍，要介於",a,"和",b)
                x=-1000
        except ValueError:
            print("輸入的不是數字")
            x=-1000
        return x
    def GAMEstart(self):
        ans = random.randint(1,99)
        low=0
        high = 100
        while True:
            while True:
                print("輸入介於",low,"及",high,"之間的數字")
                guess = input("YOUR GUESS:")
                judge_result = self.guess_judge(guess,low,high)
                if judge_result != -1000:
                    guess=int(guess)
                    break
            #print(guess)
            if guess==ans:
                print("正確答案",guess)
                break
            else:
                if guess>ans:
                    print("低一點")
                    high = guess
                else:
                    print("高一點")
                    low = guess 

gameA = GAME_GuessNumber()
gameA.GAMEstart()