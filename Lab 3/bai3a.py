for i in range(100,1001):
    check = True
    for j in range(2,int(i**0.5)+1): #Không có int(i**0.5)+1 thì không chạy được ạ :((
        if i % j == 0:
            check = False
            break
    if check == True:
        print(i, end = ' ')