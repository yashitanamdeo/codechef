# Problem Statement: https://www.codechef.com/START27C/problems/POLYBAGS

import math
T = int(input())
for _ in range(T):
    N = int(input())
    print(math.ceil(N/10))