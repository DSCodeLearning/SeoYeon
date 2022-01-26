for t in range(int(input())) :
    current_speed = 0
    result = 0

    for i in range(int(input())) :
        temp = input()
        if len(temp) == 1 : command, speed = 0, current_speed
        else : command, speed = map(int, temp.split())

        if command == 1 : current_speed += speed
        elif command == 2 :
            current_speed -= speed
            if current_speed < 0: current_speed = 0

        result += current_speed
    print(f'#{t+1} {result}')