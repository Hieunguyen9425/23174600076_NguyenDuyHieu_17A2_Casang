a = input("Nhap chuoi a: ")
b = input("Nhap chuoi b: ")
min_chuoi = a if len(a) < len(b) else b
chuoi_con = ""

for i in range(len(a)):
    for j in range(len(b)):
        k = 0
        while (i + k) < len(a) and (j + k) < len(b) and a[i + k] == b[j + k]:
            chuoi_con += a[i + k]
            k += 1
        if len(chuoi_con) > 0 and len(chuoi_con) < len(min_chuoi):
            min_chuoi = chuoi_con
        chuoi_con = ""

print(f"Chuoi ky tu chung ngan nhat cua 2 chuoi da cho la: {min_chuoi}")