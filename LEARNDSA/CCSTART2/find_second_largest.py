num1 = int(input())
num2 = int(input())
num3 = int(input())
numList = [num1,num2,num3]
maximum = max(numList[0],numList[1])
secondMax = min(numList[0],numList[1])
n = len(numList)
for i in range(2,n):
    if numList[i] > maximum:
        secondMax = maximum
        maximum = numList[i]
    elif numList[i] > secondMax and maximum!= numList[i]:
        secondMax = numList[i]
print(secondMax)