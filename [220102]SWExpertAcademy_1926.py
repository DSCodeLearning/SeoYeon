num = int(input())

for i in range(1, num+1) :
    check = 0
    for j in str(i) :
        if j == '3' or j == '6' or j == '9' : check += 1
        
    if check == 0 : print(i, end=' ')
    else : print('-'*check, end=' ')
