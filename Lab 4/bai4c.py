n = int(input("Nhap so nguyen lon hon 10 : "))
s3 = 0
a = 1
while n > 10:
    if a <= n:
        s3 += ((-1)**a)*(a**2)
    a += 1
    if a > n:
        break
print(f"S3 = {s3}")