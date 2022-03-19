# Problem Statement: https://www.codechef.com/LTIME106D/problems/SALE2

T = int(input())
for _ in range(T):
    N,X = map(int,input().split())
    count = N - (N//3)
    print(count*X)