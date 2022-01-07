for c in range(int(input())) :
    case = int(input())
    result = 0
    for i in range(1, case+1) :
        if i%2 == 0 : result -= i
        else : result += i
    print(f'#{c+1} {result}')