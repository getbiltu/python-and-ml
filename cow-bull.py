prenum=[1,2,9,4]
uin1=input("Enter ur guess:")
uin1=[]
uin1=uin

print(uin1[2])
bull=0
cow=0
for i in range(0,4):
    if (int(uin1[i])!=prenum[i]):
        bull=bull+1
    elif(int(uin1[i])==prenum[i]):
        cow=cow+1

print("Bull=",bull,"cow=",cow)
