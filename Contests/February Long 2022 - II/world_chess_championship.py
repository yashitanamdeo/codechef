# Problem Statement: https://www.codechef.com/FEB222C/problems/WCC/

T = int(input())
for _ in range(T):
    X = int(input())
    game = input()
    Ccount,Ncount,Dcount = 0,0,0
    for i in range(14):
        if game[i] == 'C':
            Ccount += 1
        if game[i] == 'N':
            Ncount += 1
        if game[i] == 'D':
            Dcount += 1
    '''
    Ccount = game.count('C')
    Ncount = game.count('N')
    Dcount = game.count('D')
    '''
    Cpoints = 2 * Ccount + (1 * Dcount)
    Npoints = 2 * Ncount + (1 * Dcount)

    if Cpoints > Npoints:
        print(60 * X)
    elif Npoints > Cpoints:
        print(40 * X)
    else:
        print(55 * X)