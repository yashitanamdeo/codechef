"""Problem Statement: https://www.codechef.com/problems/CARVANS"""

for _ in range(int(input())):
    N = int(input())
    arr = [int(i) for i in input().split()]
    
    count = 0
    Min = arr[0]
    for i in range(N):
        if arr[i] <= Min:
            Min = min(Min,arr[i])
            count += 1
    print(count)