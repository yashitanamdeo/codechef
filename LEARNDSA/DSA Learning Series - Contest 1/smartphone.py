'''Link to problem: https://www.codechef.com/LRNDSA01/problems/ZCO14003'''

N = int(input())
array = []
for i in range(N):
    budget = int(input())
    array.append(budget)

array.sort()
ansArray = []
for i in range(len(array)):
    #x = array[i]*(N-i)
    ansArray.append(array[i]*(N-i))
print(max(ansArray))