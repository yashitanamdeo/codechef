# Problem Statement: https://www.codechef.com/START31D/problems/GROUPASSGN

T = int(input())
for _ in range(T):
    N,X = map(int,input().split())
    
    ans = 2*N - X
    print(ans+1)