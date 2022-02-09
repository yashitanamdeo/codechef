T = int(input())
for _ in range(T):
    arr = list(map(int,input().split()))
    sumCountry1 = arr[0] + arr[2] + arr[4] + arr[6] + arr[8]
    sumCountry2 = arr[1] + arr[3] + arr[5] + arr[7] + arr[9]
    if sumCountry1 == sumCountry2: 
        print("0")
    elif sumCountry1 > sumCountry2:
        print("1")
    else:
        print("2")