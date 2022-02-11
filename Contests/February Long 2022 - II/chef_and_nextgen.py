# Problem Statement: https://www.codechef.com/FEB222C/problems/HELIUM3

T = int(input())
for _ in range(T):
    A,B,X,Y = map(int,input().split())
    if X*Y >= A*B:
        print("YES")
    else:
        print("NO")