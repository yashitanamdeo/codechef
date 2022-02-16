# Problem Statement: https://www.codechef.com/START26C/problems/LOSTSEQ

T = int(input())
for _ in range(T):
    N = int(input())
    B = list(map(int,input().split()))
    add = 0
    for i in range(len(B)):
        add += B[i]
    if add % 2 == 0:
        print("YES")
    else:
        print("NO")