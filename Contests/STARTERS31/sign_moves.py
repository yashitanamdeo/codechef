# Problem Statement: https://www.codechef.com/START31D/problems/SIGNMOVE

T = int(input())
for _ in range(T):
    N = int(input())
    
    if N & 1:
        answer = -1 * ((N + 1) // 2)
        print(answer)
    else:
        answer = N // 2
        print(answer)