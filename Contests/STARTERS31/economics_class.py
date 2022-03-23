# Problem Statement: https://www.codechef.com/START31D/problems/ECOCLASS

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int,input().split()))
    D = list(map(int,input().split()))
    
    count = 0
    for x in range(N):
        if S[x] == D[x]:
            count += 1
    print(count)