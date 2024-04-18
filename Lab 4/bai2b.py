so = 1
print("Cac so chinh phuong nho hon 100 : ")
while so < 100:
    uoc = 1
    while uoc * uoc <= so:
        if uoc * uoc == so:
            print(so, end = ' ') 
            break
        uoc += 1
    so += 1
