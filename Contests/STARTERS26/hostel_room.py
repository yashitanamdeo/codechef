# Problem Statement: https://www.codechef.com/START26C/problems/HOSTELROOM

T=int(input())
for _ in range(T):
    N,X = map(int,input().split())
    A = list(map(int,input().split()))
    Sum = X
    maximumSum = X
    for num in A:
        Sum += num
        maximumSum = max(Sum,maximumSum)
    print(maximumSum)