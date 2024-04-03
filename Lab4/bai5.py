while True:
    a, b = map(float, input("Nhap 2 so bat ky: ").split())
    tong = a + b
    hieu = a - b
    tich = a * b
    thuong = a / b
    luy_thua = a ** b
    sqrt_a = a ** 0.5
    sqrt_b = b ** 0.5
    
    print(f"Tong = {tong}\nHieu = {hieu}\nTich = {tich}\nThuong = {thuong}\nLuy thua = {luy_thua}\nCan bac 2 cua a = {sqrt_a}\nCan bac 2 cua b = {sqrt_b}")
    
    lua_chon = input("Ban co muon tiep tuc chuong trinh khong(y/n)? : ")
    
    while lua_chon != 'y' and lua_chon != 'n':
        lua_chon = input("Vui long chi nhap 'y' hoac 'n': ")
    
    if lua_chon == 'n':
        print("Ket thuc chuong trinh!!!")
        break
