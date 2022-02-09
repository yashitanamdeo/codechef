# Problem Statement: https://www.codechef.com/FEB221C/problems/EUREKA


import math
T = int(input())
for _ in range(T):
    N = int(input())
    value = (0.143 * N) ** N
    if (value - math.floor(value)) < 0.5:
        print(math.floor(value))
    else:
        print(math.floor(value)+1)