for t in range(int(input())) :
    P, Q, R, S, W = map(int, input().split())

    A = P * W
    if W > R : B = Q + (W-R) * S
    else : B = Q

    print(f'#{t+1} {min(A,B)}')
