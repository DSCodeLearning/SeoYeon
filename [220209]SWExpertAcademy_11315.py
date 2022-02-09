'''
이게 왜 정답이 아닌데???????????????
'''

for t in range(int(input())) :
    N = int(input())
    result = 'NO'

    case = list(range(N))
    for i in range(N) : case[i] = list(input())
    case_T = list(zip(*case))

    for i in range(N-5+1) :
        for j in range(N-5+1) :
            a, b = 0, 0
            for k in range(5):
                if (case[i+k][j+k : j+k+5] == ['o', 'o', 'o', 'o', 'o']) or (case_T[i+k][j+k : j+k+5] == ('o', 'o', 'o', 'o', 'o')):
                    result = 'YES'
                    break

                if case[i+k][j+k] == 'o' : a += 1
                if case[i+k][j+4-k] == 'o' : b += 1

            if (a == 5) or (b == 5) or (result == 'YES'):
                result = 'YES'
                break

        if result == 'YES' : break

    print(f'#{t+1} {result}')