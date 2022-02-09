T = int(input())
for _ in range(T):
    arr = list(map(int,input().split()))
    sumCountry1 = arr[0] + arr[1] + arr[2]
    sumCountry2 = arr[3] + arr[4] + arr[5]
    if sumCountry1 > sumCountry2:
        print("1")
    else:
        print("2")