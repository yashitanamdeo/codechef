T = int(input())
ans = []
for i in range(T):
    a=list(map(int,input().split()))
    x = (max(a[i-1]+a[i] for i in range(3)))
    ans.append(x)
    
for i in range(len(ans)):
    print(ans[i])