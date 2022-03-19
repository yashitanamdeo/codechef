# Problem Statement: https://www.codechef.com/LTIME106D/problems/MINCOINS

T = int(input())
for _ in range(T):
    X = int(input())
    if X % 5 != 0:
        print(-1)
    else:
        count = 0
        while X > 5:
            X -= 10
            count += 1
        if X == 0:
            print(count)
        else:
            print(count+1)