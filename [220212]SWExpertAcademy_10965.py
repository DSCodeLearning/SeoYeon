'''
거듭제곱


'''

for t in range(int(input())) :
    n = int(input())
    i = 1
    result = list()

    while i < 10**7 :
        if int((n*i)**(1/2)) == ((n*i)**(1/2)) :
            result.append(f'#{t+1} {i}')
            break
        i += 1

    print(*result, sep='\n')
    # print(n*i, int((n*i)**(1/2)) == ((n*i)**(1/2)))