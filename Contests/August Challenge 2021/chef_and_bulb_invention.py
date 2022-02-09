for _ in range(int(input())):
    N,P,K = map(int,input().split())
    ans = 0
    
    a = P%K - 1
    b = ((N-1)//K)*K
    b = N-1-b
    
    if(a>b):
        ans += (b+1)*((N-1)//K+1) + (a-b)*((N-1)//K)
    else:
        ans += ((N-1)//K+1)*(a+1)
        
    for i in range(a+1,N,K):
        ans += 1
        if(i==P):
            print(ans)
            break