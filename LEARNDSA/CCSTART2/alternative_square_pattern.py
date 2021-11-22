'''Problem Statement: https://www.codechef.com/CCSTART2/problems/SQALPAT'''

N = int(input())
k = -4
for i in range(1,N+1):
    if i%2!=0:
        k+=4
        for j in range(1,6):
            k+=1
            print(k,end=" ")
        print("")
    else:
        k+=6
        for j in range(1,6):
            k-=1
            print(k,end=" ")
        print("")
