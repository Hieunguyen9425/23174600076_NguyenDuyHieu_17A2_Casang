n = int(input("Nhap n: "))
nguyen_to = [so for so in range(2, 100) if all(so % i != 0 for i in range(2, int(so ** 0.5) + 1))][:n]
print(f"Danh sach {n} so nguyen to dau tien: {nguyen_to}")
