do = 20
xanh = 15
vang = 15
bi = 50
so_bi_rut = int(input("Nhap so bi muon rut : "))
xac_suat_do = (do/bi) ** so_bi_rut #Xac suat bi do
xac_suat_xanh = 1 - ((bi - xanh)/bi) ** so_bi_rut #Xac suat bi xanh
print(f"Xac suat tat ca la bi do : {xac_suat_do}\nXac suat it nhat 1 xanh : {xac_suat_xanh} ")
