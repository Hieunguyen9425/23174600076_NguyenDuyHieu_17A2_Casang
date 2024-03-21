do_dai_canh_day, chieu_cao_chop = map(int, input("Nhap do dai canh day va chieu cao cua hinh chop(Cach nhau bang khoang trong) : ").split())
nua_chu_vi_day = do_dai_canh_day * 2
s_day = do_dai_canh_day * 4
s_xung_quanh = nua_chu_vi_day * chieu_cao_chop
s_toan_phan = s_xung_quanh + s_day
v_chop = 1/3 * (s_day * chieu_cao_chop)
print(f"Dien tich xung quanh la : {s_xung_quanh:.2f}, dien tich toan phan la {s_toan_phan:.2f}, the tich la {v_chop:.2f}")