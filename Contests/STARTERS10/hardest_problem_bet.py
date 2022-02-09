T = int(input())
for _ in range(T):
    problem = list(map(int,input().split()))
    if min(problem) == problem[1]:
        print("Bob")
    elif min(problem) == problem[2]:
        print("Alice")
    else:
        print("Draw")