# Problem Statement: https://www.codechef.com/START28C/problems/SUNDAY

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    
    holidays = [6,7,13,14,20,21,27,28]
    total_holidays = 8
    for i in range(N):
        if A[i] not in holidays:
            total_holidays += 1
    
    print(total_holidays)