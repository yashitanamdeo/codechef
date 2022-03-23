# Problem Statement: https://www.codechef.com/START31D/problems/ALTSTR

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input())

    count_of_zero = S.count('0')
    count_of_one = S.count('1')

    
    if S == '0'*N or S == '1'*N:
        print(1)
        continue
    num = min(count_of_zero,count_of_one)
    if count_of_zero == count_of_one:
        print(count_of_zero + count_of_one)
        continue
    else:
        print((2 * num) + 1)