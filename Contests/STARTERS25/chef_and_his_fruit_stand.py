# Problem Statement: https://www.codechef.com/START25C/problems/FRUITCHAAT

T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    banana = X//2
    if Y > banana:
        print(banana)
    else:
        print(Y)