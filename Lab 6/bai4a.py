n = int(input("Nhap vao so n: "))
a = [0, 1]
[a.append(a[-1] + a[-2]) for _ in range(2,n + 1)]
print(a)