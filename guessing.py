import random as rnd

rndm=rnd.randint(1,99)
#print(rndm)
uin=input("Enter Gussing number:")
count=1
if(int(uin)!=rndm):
    while(rndm!=int(uin)):
        if(int(uin)>rndm):
            print(":::Decrease Number:::\n")
            uin=input("Enter new Number:")
            count = count + 1
        elif(int(uin)<rndm):
            print("::increase Number:::\n")
            uin=input("Enter new Number:\n")
            count = count + 1
        if(int(uin)==rndm):
            print("Matched")
            print("Attemped", count)
            print("Random Number:",rndm)


else:
    print("Matched")
    print("Attemped",count)
    print("Random Number:", rndm)