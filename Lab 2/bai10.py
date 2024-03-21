lua_chon_phim = int(input("Nhap so tuong ung voi the loai phim\n1.Hanh dong\n2.Kinh di\n3.Tinh cam\n4.Hai huoc\n5.Hoat hinh\n"))
if lua_chon_phim == 1:
    print("Da chon the loai Hanh dong(Trinh chieu ca ngay)")
    time = int(input("Chon suat chieu(Nhap so gio) : "))
    print(f"Chuc ban xem phim vui ve. Hay quay lai vao luc {time}h!!!")
elif lua_chon_phim == 2:
    print("Da chon the loai Kinh di(Suat chieu tu 18h den 24h)")
    time = int(input("Chon suat chieu(Nhap so gio) : "))
    if 18 <= time <= 24:
        print(f"Chuc ban xem phim vui ve. Hay quay lai vao luc {time}h!!!")
    else:
        print("Không có suất chiếu")
elif lua_chon_phim == 3:
    print("Da chon the loai Tinh cam(Suat chieu tu 18h den 24h)")
    time = int(input("Chon suat chieu(Nhap so gio) : "))
    if 18 <= time <= 24:
        print(f"Chuc ban xem phim vui ve. Hay quay lai vao luc {time}h!!!")
    else:
        print("Không có suất chiếu")
elif lua_chon_phim == 4:
    print("Da chon the loai Hai huoc(Trinh chieu ca ngay)")
    time = int(input("Chon suat chieu(Nhap so gio) : "))
    print(f"Chuc ban xem phim vui ve. Hay quay lai vao luc {time}h!!!")
elif lua_chon_phim == 5:
    print("Da chon the loai Hoat hinh(Suat chieu tu 8h den 15h)")
    time = int(input("Chon suat chieu(Nhap so gio) : "))
    if 8 <= time <= 15:
        print(f"Chuc ban xem phim vui ve. Hay quay lai vao luc {time}h!!!")
    else:
        print("Không có suất chiếu")   
else:
    print("Lua chon khong hop le")

