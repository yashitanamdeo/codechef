# Problem Statement: https://www.codechef.com/START27C/problems/BINSTRING

# Accepted
T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    count = N

    for i in range(1,N):
        if S[i] == S[i-1]:
            count -= 1
    print(count)

# RTE(other)
T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    memory = []
    new = ''

    for i in range(N):
        new = S[:i] + S[i+1:]
        memory.append(new)

    memory_set = set(memory)
    #print(memory)
    #print(memory_set)
    print(len(memory_set))