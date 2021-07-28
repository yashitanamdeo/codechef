import math
    
T = int(input())
finalans =[]
ans = 0
for _ in range(T):
    A,B = map(int,input().split())
    if (A%2==0 and B%2 == 0):
        ans = 0
        finalans.append(ans)
    elif (math.gcd(A,B)!=1):
        ans = 0
        finalans.append(ans)
    elif (math.gcd(A+1,B)>1 or (math.gcd(A,B+1)>1)):
        ans = 1
        finalans.append(ans)
    else:
        ans = 2
        finalans.append(ans)

for i in range(len(finalans)):
    print(finalans[i])