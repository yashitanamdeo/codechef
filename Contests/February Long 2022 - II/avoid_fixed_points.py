# Problem Statement: https://www.codechef.com/FEB222C/problems/NOFIX

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for i in range(N):
        value = i+1+count
        if arr[i] == value:
            count += 1
    print(count)