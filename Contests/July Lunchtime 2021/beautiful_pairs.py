T = int(input())
for x in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    arr = {}
    for x in A:
        if x in arr.keys():
            arr[x] = arr[x] + 1
        else:
            arr[x] = 1
        
    length = len(A)
    ans = 0
    for key in arr.keys():
        ans += arr[key] * (length-arr[key])
    
    print(ans)