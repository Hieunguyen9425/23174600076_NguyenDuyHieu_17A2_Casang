n = int(input("Nhap so luong so nguyen n: "))
ds = [int(input(f"Nhap vao phan tu thu {i + 1}: ")) for i in range (n)]
khoang_cach = [ds[i + 1] - ds[i] for i in range(1, len(ds)- 1)]
check = all(kc ==  khoang_cach[0] for kc in khoang_cach)
if check:
    print("Day so la cap so cong")
else:
    print("Day so khong la cap so cong")