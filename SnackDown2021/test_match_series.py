n = int(input())
for _ in range(n):
    test = list(map(int,input().split()))
    if test.count(1) > test.count(2):
        print("INDIA")
    elif test.count(2) > test.count(1):
        print("ENGLAND")
    else:
        print("DRAW")