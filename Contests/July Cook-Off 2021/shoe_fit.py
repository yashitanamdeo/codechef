T = int(input())
ans = []
for _ in range(T):
    A,B,C = map(int,input().split())
    if A*B*C == 0 and (A+B+C) > 0:
        ans.append("1")
    else:
        ans.append("0")

for i in range(len(ans)):
    print(ans[i])