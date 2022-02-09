for t in range(int(input())) :
    P, Q = input().strip(), input().strip()

    if P+'a' == Q : print(f'#{t+1} N')
    else : print(f'#{t+1} Y')