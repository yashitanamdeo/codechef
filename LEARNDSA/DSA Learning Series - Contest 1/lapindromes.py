T = int(input())
for _ in range(T):
    word = input()
    length = len(word)
    dict1={}
    dict2={}
    mid = length//2
    for i in range(0,mid):
        x = word[i]
        if x in dict1:
            dict1[x]+=1
        else:
            dict1[x]=1
    if length%2!=0:
        mid+=1
    for j in range(mid,length):
        x = word[j]
        if x in dict2:
            dict2[x]+=1
        else:
            dict2[x]=1
    
    if dict1==dict2:
        print("YES")
    else:
        print("NO")