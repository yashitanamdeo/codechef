N = int(input())
myList = list(map(int,input().split()))
myList.reverse()

for i in myList:
    print(i, sep=" ", end=" ")