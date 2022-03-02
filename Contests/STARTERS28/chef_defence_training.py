# Problem Statement: https://www.codechef.com/START28C/problems/SELFDEF

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    
    count = 0
    for i in range(N):
        if arr[i] in range(10,61):
            count += 1
    print(count)