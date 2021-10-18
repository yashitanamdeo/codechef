n = int(input())
for _ in range(n):
    numList = list(map(int,input().split()))
    if 7 in numList:
        print("YES")
    else:
        print("NO")