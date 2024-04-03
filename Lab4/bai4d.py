n = int(input("Nhap so nguyen lon hon 10 : "))
s4 = 0
a = 1
while n > 10:
    if a <= n:
        s4 += a*(a+1)*(a+2)
    a += 1
    if a > n:
        break
print(f"S4 = {s4}")