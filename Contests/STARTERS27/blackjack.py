# Problem Statement: https://www.codechef.com/START27C/problems/BLACKJACK

T = int(input())
for _ in range(T):
    A,B = map(int,input().split())
    a_plus_b = A + B
    balance = 21 - a_plus_b
    if balance <= 10:
        print(balance)
    else:
        print(-1)