a = input("Nhap chuoi: ")
b = ""
for i in a:
    if i.isnumeric():
        b += i
print(f"Chuoi sau khi duoc tach: {b}")
so_b = int(b)
check = True

if so_b < 2:
    check = False
else:
    for i in range(2, int(so_b**0.5) + 1):
        if so_b % i == 0:
            check = False
            break

if check:
    print("Chuoi la so nguyen to")
else:
    print("Chuoi khong la so nguyen to")