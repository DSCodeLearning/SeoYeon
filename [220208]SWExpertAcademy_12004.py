for t in range(int(input())) :
    n = int(input())
    result = 'No'
    for i in range(1, 10) :
        if (n/i == n//i) and (1 <= n//i <= 9) :
            result = 'Yes'

    print(f'#{t+1} {result}')
