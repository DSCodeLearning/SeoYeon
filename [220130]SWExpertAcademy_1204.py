for t in range(int(input())) :
    N = int(input())
    case = sorted(list(map(int, input().split())))
    temp, result = [0, 0], [0, 0]

    for c in case :
        if c == temp[0] :
            temp[1] += 1
            if temp[1] >= result[1] :
                result = temp.copy()
        else :
            temp = [c, 1]

    print(f'#{N} {result[0]}')