so_nguoi = int(input("Nhap so nguoi : "))
gia_goc = 120000
if so_nguoi == 1:
    tong_tien = 120000
elif 1 < so_nguoi <= 4:
    tong_tien = (gia_goc * so_nguoi) - (gia_goc * so_nguoi)*0.05
elif 4 < so_nguoi <= 10:
    tong_tien = (gia_goc * so_nguoi) - (gia_goc * so_nguoi)*0.1
else:
    tong_tien = (gia_goc * so_nguoi) - (gia_goc * so_nguoi)*0.2
print(f"So tien phai tra la {tong_tien} vnd")