import random as rnd
random=rnd.randint(1000,9999)
guess=[]
guess=str(random)

uin=input("Enter ur guess Of 4 digit:")
uin1=[]
uin1=uin

bull=0
cow=0
for i in range(0,4):
    if(int(uin1[i])!=int(guess[i])):
        bull=bull+1
    elif(int(uin1[i])==int(guess[i])):
        cow=cow+1

print("Bull=",bull,"cow=",cow,"\nand Number Is:",random)
