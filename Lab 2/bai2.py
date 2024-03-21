so = int(input("Nhap so bat ki : "))
if 1000 <= so <= 9999 :
    chu_so_hang_nghin = so // 1000
    print(f"Chu so hang nghin cua so {so} la {chu_so_hang_nghin}")
else:
    print("0")