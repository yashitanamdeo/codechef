# Problem Statement: https://www.codechef.com/LTIME106D/problems/CREDCOINS

T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    product = X*Y
    print(product//100)