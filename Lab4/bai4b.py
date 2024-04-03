n = int(input("Nhap so nguyen lon hon 10 : "))
s2 = 0
a = 1
while n > 10:
    if a <= n and a % 2 != 0:
        s2 += 1 / (3 ** a)
    a += 1
    if a > n:
        break
print(f"S2 = {s2}")
