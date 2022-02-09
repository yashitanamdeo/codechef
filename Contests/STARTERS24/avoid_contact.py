# Problem Statement: https://www.codechef.com/START24C/problems/AVOIDCONTACT

T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    diff = X-Y
    if Y == 0:
        print(X)
    else:
        if X>Y:
            print((Y*2) + diff)
        else:
            print((Y*2) - 1)