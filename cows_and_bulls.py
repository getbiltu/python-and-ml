import random as rnd
randnum=rnd.randint(1000,9999)
generated_num=[]
generated_num=str(randnum)
bull=0
cow=0
count=0

def display(cow,bull,count):#display function for display outcomes on Every guess
    if cow==4 :
        print(":::::Congrats You Have Guessed Correctly:::::\nNumber Is:", generated_num,"\nCow=",cow," bull=",bull,"\nAttemped=",count)
    else:
        print(":::::Try Again:::::\nCow=",cow," bull=", bull,"\nAttemped=", count)

usr_in=input("Enter 4 Digit Guess Number:")

while generated_num!=usr_in:
    for i in range(0,4):
        if(int(usr_in[i])!=int(generated_num[i])):
            bull+=1
        else:
            cow+=1

    count+=1
    display(cow,bull,count)
    cow=0
    bull=0
    usr_in = input("Enter 4 Digit Guess Number Again:")

if generated_num==usr_in:
    cow=4
    count+=1
    display(cow,bull,count)
