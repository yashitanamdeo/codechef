T = int(input())
ans = []
for i in range(T):
    a,b = map(int,input().split())
    sum = a+b
    if sum<3:
        ans.append("1")
    elif 3 <= sum and sum <= 10:
        ans.append("2")
    elif 11 <= sum and sum <= 60:
        ans.append("3")
    elif 60 < sum:
        ans.append("4")
for i in ans:
    print(i)
    