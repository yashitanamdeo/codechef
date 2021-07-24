N = int(input())
if N%5 == 0:
    if N%11 == 0:
        print("BOTH")
    if N%11 != 0:
        print("ONE")
elif N%11 == 0:
    if N%5 != 0:
        print("ONE")
else:
    print("NONE")