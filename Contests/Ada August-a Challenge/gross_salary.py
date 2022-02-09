T = int(input())
for _ in range(T):
    salary = int(input())
    basicSalary = salary
    if salary < 1500:
        HRA = (10/100)*basicSalary
        DA = (90/100)*basicSalary
    elif salary >= 1500:
        HRA = 500
        DA = (98/100)*basicSalary
    grossSalary = basicSalary + HRA + DA
    print(grossSalary)