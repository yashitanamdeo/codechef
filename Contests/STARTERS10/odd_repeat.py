T = int(input())
for _ in range(T):
    N,K,S = map(int,input().split())
    S = S - (N*N)
    print(S//(K-1))