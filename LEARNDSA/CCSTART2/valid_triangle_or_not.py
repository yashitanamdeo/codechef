a,b,c = map(int,input().split())

s = (a+b+c)//2 #semi perimeter
area = (s*(s-a)*(s-b)*(s-c))**1/2 #heron's formula

if a+b>=c and a+c>=b and b+c>=a: #sum of 2 sides must be greater than or equal to the third side
    if area>0:
        print("YES")
else:
    print("NO")