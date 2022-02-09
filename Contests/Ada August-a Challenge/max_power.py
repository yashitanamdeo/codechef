length = int(input())
string = input()
ans = 0

for i in range(length-1,-1,-1):
    if (string[i] == '0'):
        ans+=1
    else:
        break
print(ans)