n = int(input("Nhap so luong so nguyen n: "))
ds = [int(input(f"Nhap vao phan tu thu {i + 1}: ")) for i in range (n)]
ds_chan = []
ds_le = []
tong_chan = 0
tong_le = 0
for a in ds:
    if a % 2 == 0:
        ds_chan.append(a)
        tong_chan += a
    else:
        ds_le.append(a)
        tong_le += a
print(f"Mang gom cac so chan {ds_chan}")
print(f"Tong cac so chan trong mang: {tong_chan}")
print(f"Mang gom cac so le {ds_le}")
print(f"Tong cac so le trong mang: {tong_le}")