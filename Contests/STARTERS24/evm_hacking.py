# Problem Statement: https://www.codechef.com/START24C/problems/EVMHACK


T = int(input())
for _ in range(T):
    A,B,C,P,Q,R = map(int,input().split())
    condition = (P+Q+R)/2
    if A+B+R > condition: #hacking EVM of city3
        print("YES")
    elif A+Q+C > condition: #hacking EVM of city2
        print("YES")
    elif P+B+C > condition: #hacking EVM of city1
        print("YES")
    else:
        print("NO")