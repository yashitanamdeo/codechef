T = int(input())
for _ in range(T):
    A,B,C = map(int,input().split())
    angleSum = A+B+C
    if angleSum == 180:
        print("YES")
    else:
        print("NO")