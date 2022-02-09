# Problem Statement: https://www.codechef.com/START25C/problems/POLIN

T = int(input())
for _ in range(T):
    N = int(input())
    Xpoints,Ypoints = [],[]
    for i in range(N):
        Xi,Yi = map(int,input().split())
        Xpoints.append(Xi)
        Ypoints.append(Yi)
    
    print(len(set(Xpoints)) + len(set(Ypoints)))