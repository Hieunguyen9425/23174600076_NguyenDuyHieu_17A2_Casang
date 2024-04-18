tong = 0
so_da_nhap = ""
so_le = ""
so_chan = ""
a = 0
while True:
    so = int(input("Nhap so nguyen duong : "))
    a += 1
    so_da_nhap += str(so) + " " # Cac so da nhap tu ban phim
    if so <= 0:
        break
    tong += so
    if so % 2 != 0: 
        so_le += str(so) + " " #Cac so le da nhap
    if so % 2 == 0:
        so_chan += str(so) + " " #Cac so chan da nhap
    if tong > 1000:
        break
print(f"Các số đã nhập từ bàn phím l: {so_da_nhap}\nCác số lẻ đã nhập là: {so_le}\nCác số chẵn đã nhập là: {so_chan}\nSố lượng số nguyên đã nhập: {a}")
