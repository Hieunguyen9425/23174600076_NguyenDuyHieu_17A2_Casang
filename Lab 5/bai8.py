chuoi = input("Nhap chuoi: ")
if len(chuoi) <= 10:
    print("vui long nhap chuoi co do dai lon hon 10")
else:
    chuoi_a = chuoi[1:8] #a
    print(chuoi_a)
    chuoi_b = chuoi[4:9]#b
    print(chuoi_b)
    chuoi_c = chuoi[-3:] #c
    print(chuoi_c)
    chuoi_thuong = chuoi.lower() #d
    print(chuoi_thuong)
    chuoi_hoa = chuoi.upper() #e
    print(chuoi_hoa)
    chuoi_dao_nguoc = chuoi[::-1] #f
    print(chuoi_dao_nguoc)