# Problem Statement: https://www.codechef.com/COOK139C/problems/JGAMES

T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    if (X+Y) % 2 == 0:
        print("Janmansh")
    else:
        print("Jay")