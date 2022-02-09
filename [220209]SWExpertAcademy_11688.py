for t in range(int(input())) :
    way = list(input())
    d, m = 1, 1
    for w in way :
        if w == 'L' : d, m = d, d+m
        else : d, m = d+m, m

    print(f'#{t+1} {d} {m}')
