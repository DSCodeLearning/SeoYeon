for t in range(int(input())) :
    day = input()
    case = {'MON' : 6, 'TUE' : 5, 'WED' : 4, 'THU' : 3, 'FRI' : 2, 'SAT' : 1, 'SUN' : 7 }
    print(f'#{t+1} {case[day]}')