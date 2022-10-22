import random
import os
import time

sy = ['#','$','%','&','@','£','€']
sy_val = [5,10,20,70,200,1000,1000_000]
sy_prob = [50,40,30,20,10,5,1]
sy_prob_base = 156
sy_holder = []

for i in range(len(sy)):
    sy_holder += [sy[i]]*sy_prob[i]


class SlotMachine:
    reels = [sy[-1],sy[-1],sy[-1]]

    def __init__(self):
        pass

    
    def spin(self):
        self.reels[0] = random.choice(sy_holder)
        self.reels[1] = random.choice(sy_holder)
        self.reels[2] = random.choice(sy_holder)   

    def prize(self, bet):
        if(not(self.reels[0] == self.reels[1] and self.reels[0] == self.reels[2])):
            return 0
        for i in range(len(sy)):
            if(self.reels[0] == sy[i]):
                return bet*sy_val[i]

    def play(self, bet):
        self.spin()
        return self.prize(bet)

    
    def __str__(self) -> str:
        return ("---------------------------\n"+
                "---------------------------\n"+
                "---------------------------\n"+
                f"-----| {self.reels[0]} |-| {self.reels[1]} |-| {self.reels[2]} |-----\n"+
                "---------------------------\n"+
                "---------------------------\n"+
                "---------------------------")
        
    
os.system('clear')

while(True):
    try:
        credit = int(input("How many credits do you want to use? -> "))
    except ValueError:
        print("Input must be an integer")
        continue
    else:
        if(credit <= 0):
            print("Ammount must be positive")
            continue
        break

slot = SlotMachine()

while(credit > 0):
    print(f"\nCredits: {credit}\n")
    while(True):
        go = input("Do you want to keep playing?(y/n) -> ")
        if(go == "y"):
            break
        elif(go == "n"):
            quit()
        else:
            print("Answer must be y or n")
    
    while(True):
        try:
            bet = int(input("How much do you want to bet? -> "))
        except ValueError:
            print("Input must be an integer")
            continue
        else:
            if(bet <= 0):
                print("Ammount must be positive")
                continue
            elif(bet > credit):
                print(f"You don't have enough credit for that bet (Credit = {credit})")
                continue
            break
    credit -= bet
    credit += slot.play(bet)
    os.system('clear')
    print(slot)

print("\nYou ran out of credits. Goodbye\n")

time.sleep(10)
os.system('clear')
print("\n\n\n SUCKEEEEERR \n\n\n")
