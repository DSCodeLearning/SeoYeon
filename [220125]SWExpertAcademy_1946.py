for t in range(int(input())) :
    N = int(input())
    letter = ['']*N
    num = [0]*N
    for n in range(N) :
        letter[n], num[n] = input().split()
        num[n] = int(num[n])

    temp = 0
    print(f'#{t+1}')
    for i in range(N) :
        for j in range(num[i]) :
            print(letter[i], end='')
            temp += 1
            if temp == 10 :
                print()
                temp = 0
    print()