hieu_dien_the = 220
cuong_do_dong_dien = 1.5
cong_suat = hieu_dien_the * cuong_do_dong_dien
so_gio = int(input("Nhap so gio su dung : "))
tong_so_gio = so_gio * 5000
tong_tien = (cong_suat * tong_so_gio) / 1000 #1kWh = 1000Wh
print(f"So tien phai tra la : {tong_tien} vnd")