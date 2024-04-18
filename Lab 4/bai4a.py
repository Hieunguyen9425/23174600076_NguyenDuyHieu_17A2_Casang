n = int(input("Nhap so nguyen lon hon 10 : "))
s1 = 0
a = 1
while n > 10:
    if a <= n:
        s1 += 6**a
        a += 1
    else:
        break
print(f"S1 = {s1}")