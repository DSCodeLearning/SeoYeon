casenum = int(input())
case = [int(input()) for i in range(casenum)]

def Factorial(n) :
    if n == 0 :
        return 1
    elif n == 1 :
        return 1
    return n * Factorial(n-1)

for i in range(casenum) :
    print(f'#{i+1}')
    for j in range(0, case[i]) :
        for k in range(j+1) :
            print(Factorial(j) // (Factorial(j-k) * Factorial(k)), end=' ')
        print()