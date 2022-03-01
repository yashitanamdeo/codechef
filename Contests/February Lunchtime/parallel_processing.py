# Problem Statement: https://www.codechef.com/LTIME105C/problems/PLPROCESS

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    sumA = 0
    array = [0] * N
    
    for i in range(N):
        sumA += A[i]
        array[i] = sumA
    
    answer = sumA
    for i in range(N):
        answer = min(max(array[i], sumA - array[i]), answer)
    print(answer)