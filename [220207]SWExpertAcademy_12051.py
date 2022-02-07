for t in range(int(input())) :
    N, Pd, Pg = map(int, input().split())
    result = 'Broken'
    if (Pd != 100 and Pg == 100) or (Pd != 0 and Pg == 0) : result = 'Broken'
    else :
        for n in range(1, N+1) :
            if n*Pd/100 == n*Pd//100 :
                result = 'Possible'
                break

    print(f'#{t+1} {result}')