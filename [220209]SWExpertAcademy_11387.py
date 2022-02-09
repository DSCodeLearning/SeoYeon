for t in range(int(input())) :
    D, L, N = map(int, input().split())
    print(f'#{t+1} {int(D * N + (D * L * N * (N-1)) / 200)}')

