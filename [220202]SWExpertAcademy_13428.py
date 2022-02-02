for t in range(int(input())) :
    n = [ i for i in input()]
    case = [int(''.join(n))]

    for i in range(len(n)):
        for j in range(i):
            temp = n.copy()
            temp[i], temp[j] = temp[j], temp[i]

            if (temp not in case) and (temp[0] != '0') : case.append(int(''.join(temp)))
            else : continue

    print(f'#{t+1} {min(case)} {max(case)}')