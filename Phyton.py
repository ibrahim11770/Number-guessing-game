# Game using while loop
import random
num=random.randint(1,10)
tries=0
while True:
    guess=int(input("enter any number between 1 to 10: "))
    if num==guess:
         tries+=1
         print(f"you are right you guess this number in {tries} tries")
         break
       
    elif num<guess:
         tries+=1
         print("go a littel low")
       
    elif num>guess:
         tries+=1
         print("go a littel high")
     elif num==guess: 
         print(f"you guess this number in {tries} tries")
         break
    else:
           tries+=1
           print(f"you are wrong you guess this number in {tries} tries")
