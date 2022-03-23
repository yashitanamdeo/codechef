# Problem Statement: https://www.codechef.com/START31D/problems/CRICUP

T = int(input())
for _ in range(T):
    X,Y,D = map(int,input().split())
    
    if abs(X - Y) <= D:
        print("YES")
    else:
        print("NO")