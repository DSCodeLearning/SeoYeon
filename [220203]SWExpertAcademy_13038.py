for t in range(int(input())) :
    p = int(input())
    week = list(map(int, input().split()))
    result = 0

    for i in range(7) :
        d, n, temp = i, p, 0

        while n != 0 :
            temp += 1
            if week[d] == 1 : n -= 1

            if d == 6 : d = 0
            else : d += 1

        if i == 0 : result = temp
        else : result = min(result, temp)

    print(f'#{t+1} {result}')