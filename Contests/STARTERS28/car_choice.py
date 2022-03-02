# Problem Statement: https://www.codechef.com/START28C/problems/CARCHOICE

T = int(input())
for _ in range(T):
    x1,x2,y1,y2 = map(int,input().split())
    
    c1_cost = y1/x1
    c2_cost = y2/x2
    
    if c1_cost == c2_cost:
        print("0")
    elif c1_cost < c2_cost:
        print("-1")
    else:
        print("1")