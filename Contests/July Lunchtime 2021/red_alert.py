T = int(input())
for x in range(T):
    N, D, H = map(int,input().split())
    arr=list(map(int,input().split()))
    waterlevel = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            waterlevel += arr[i]
        else:
            if waterlevel < D:
                waterlevel = 0
            else:
                waterlevel -= D
        if waterlevel > H:
            print("YES")
            break
    else:
        print("NO")