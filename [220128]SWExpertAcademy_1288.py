for t in range(int(input())) :
    N = int(input())
    num = [0,1,2,3,4,5,6,7,8,9]
    i = 1

    while len(num) != 0 :
        txt = str(i * N)
        for k in txt :
            if int(k) in num : num.remove(int(k))
        i += 1

    print(f'#{t+1} {(i-1)*N}')