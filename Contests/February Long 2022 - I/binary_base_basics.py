# Problem Statement: https://www.codechef.com/FEB221C/problems/BINBASBASIC

# cook your dish here
T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    S = str(input())
    
    i = 0
    j = N - 1
    notEqualCount = 0
    while(i<j):
        if S[i] != S[j]:
            notEqualCount += 1
        i += 1
        j -= 1        
    
    if notEqualCount <= K:
        if N%2 == 1:
            print("YES")
        elif (K-notEqualCount)%2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
