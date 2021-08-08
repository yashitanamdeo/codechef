T = int(input())
for _ in range(T):
    arr = list(map(int,input().split()))
    problems = set(arr)
    if len(problems)==4 or len(problems)==3:
        print("2")
    elif len(problems)==2:
        if arr.count(arr[0]) == 2: 
            print("2") #ultimately len is minimum 3 hence output is 2
        else:
            print("1") #here there are 3 same numbers hence output is 1
    else:
        print("0")