# Problem Statement: https://www.codechef.com/START27C/problems/PRODUCT

import math
T = int(input())
for _ in range(T):
    B,C = map(int,input().split())
    print(C//math.gcd(B,C))