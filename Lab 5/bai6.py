chuoi = input("Nhap mot chuoi: ")
dem_ky_tu_dac_biet = {}
tong_so_ky_tu = len(chuoi)
for ky_tu in chuoi:
    if not ky_tu.isalnum():
        if ky_tu in dem_ky_tu_dac_biet:
            dem_ky_tu_dac_biet[ky_tu] += 1
        else:
            dem_ky_tu_dac_biet[ky_tu] = 1
for ky_tu in dem_ky_tu_dac_biet:
    so_lan_xuat_hien = dem_ky_tu_dac_biet[ky_tu]
    ty_le_phan_tram = so_lan_xuat_hien / tong_so_ky_tu * 100
    print(f"Ky tu dac biet {ky_tu} xuat hien {so_lan_xuat_hien} lan ({ty_le_phan_tram:.2f}% trong chuoi)")
