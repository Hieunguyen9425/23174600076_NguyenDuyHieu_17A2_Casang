so = 2
print("Cac so nguyen to nho hon 100 : ")
while so < 100:
    check = True
    uoc = 2
    while uoc * uoc <= so:
        if so % uoc == 0:
            check = False
            break
        uoc += 1
    if check:
        print(so, end = ' ')
    so += 1 