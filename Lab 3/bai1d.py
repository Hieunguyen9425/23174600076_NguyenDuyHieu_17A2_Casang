s4 = 0
n = int(input("Nhap n : "))
if n <= 0:
    print("Xin moi nhap lai!!!")
for i in range(1,n+1):
    s4 += ((-1)**(i+1))/i
print(s4)