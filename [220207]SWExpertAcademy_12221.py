for t in range(int(input())) :
    a, b = map(int, input().split())
    if a>=10 or b>=10 : print(f'#{t+1} -1')
    else : print(f'#{t+1} {a*b}')