import random as rd
rn = rd.randint(1, 10)
count = 0
while(True):
    rn = rd.randint(1, 10)
    for i in range(3):
        n = int(input("Enter a number from 1 to 10:"))
        count += 1
        if(rn == n):
            print("you won!")
            break
        if(count >= 3):
            print("you have lost")
            ans = input("wanna play again?")
            if(ans == "yes"):
                rn = rd.randint(1, 10)
            else:
                break
