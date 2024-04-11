chuoi = input("Nhap mot chuoi: ")
so_luong_chu_thuong = 0
so_luong_chu_in_hoa = 0
so_luong_chu_so = 0
ky_tu_dac_biet = 0
for ky_tu in chuoi:
    if ky_tu.islower():
        so_luong_chu_thuong += 1
    if ky_tu.isupper():
        so_luong_chu_in_hoa += 1
    if ky_tu.isnumeric():
        so_luong_chu_so += 1
    if not ky_tu.isalnum():
        ky_tu_dac_biet += 1
print(f"Co {so_luong_chu_thuong} chu thuong\n{so_luong_chu_in_hoa} chu in hoa\n{so_luong_chu_so} chu so\n{ky_tu_dac_biet} ky tu dac biet")

