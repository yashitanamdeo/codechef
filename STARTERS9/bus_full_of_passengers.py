for _ in range(int(input())):
    N,M,Q = map(int,input().split())
    flag = 1
    x = []
    
    for i in range(Q):
        ch, entry = input().split()

        entry = int(entry)
        if(ch=="-" and (entry not in x)):
            flag = 0
            continue
        if(ch=="+" and (len(x)>=M)):
            flag = 0
            continue
        if(ch=="+" and (entry not in x) and (len(x)<M)):
            x.append(entry)
        if(ch=="-" and (entry in x)):
            x.remove(entry)
    
    if(flag == 1):
        print("Consistent")
    else:
        print("Inconsistent")
    
        
        
        
# approach 1        
''' 
        ans = "Consistent"
        while(True):
            if total <= M:
                first = 0
                if ch == "+":
                    total += entry
                    first = 1
                    if total > M:
                        ans = "Inconsistent"
                else:
                    if first != 0:
                        total -= entry
                    else:
                        x = 1
                        ans = "Inconsistent"
            elif x == 1:
                ans = "Inconsistent"
            break
    print(ans)
    
'''