# Problem Statement: https://www.codechef.com/LTIME105C/problems/NIBBLE

T = int(input())
for _ in range(T):
    N = int(input())
    if N%4 == 0:
        print("Good")
    else:
        print("Not Good")