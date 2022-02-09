# Problem Statement: https://www.codechef.com/START25C/problems/DATATYPE

T = int(input())
for _ in range(T):
    N,X = map(int,input().split())
    if X <= N:
        print(X)
    else:
        while(X > N):
            X = X-N-1
        print(X)