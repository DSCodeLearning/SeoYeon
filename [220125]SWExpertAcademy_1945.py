num = [2, 3, 5, 7, 11]
for t in range(int(input())) :
    case = int(input())

    print(f'#{t+1}', end=' ')
    for i in range(len(num)):
        result = 0
        while case % num[i] == 0:
            case /= num[i]
            result += 1
        print(result, end=' ')
    print()