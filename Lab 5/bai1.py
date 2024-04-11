chuoi = ""
n = int(input("Nhap vao so nguyen: "))

if n < 0:
    print("Nhap lai so khac")
else:
    while n > 0:
        phan_du = n % 2
        chuoi = str(phan_du) + chuoi
        n //= 2
    print("Chuyen so tu he 10 sang he nhi phan duoc:", chuoi)