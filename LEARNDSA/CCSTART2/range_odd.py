L,R = map(int,input().split())
oddNum = []
for num in range(L,R+1):
    if num%2 != 0:
        oddNum.append(num)

for i in oddNum:
    print(i,sep=" ",end=" ")