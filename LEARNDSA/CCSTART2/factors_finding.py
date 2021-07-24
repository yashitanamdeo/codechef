N = int(input())
factors = []
count = 0
for num in range(1,N+1):
    if N % num == 0:
        count += 1
        factors.append(num)
        
print(count)
for i in factors:
    print(i, sep=" ", end=" ")