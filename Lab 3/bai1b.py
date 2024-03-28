s2 =0
n = int(input("Nhap n : "))
if n <= 0:
    print("Xin moi nhap lai!!!")
for i in range(1,n+1):
    s2 += 1/i
print(s2)