import math
x,y = map(float, input("Nhap toa do tam duong tron : ").split())
a,b = map(float, input("Nhap he so goc va he so tu do cua duong thang ").split())
r = float(input("Nhap ban kinh duong tron : "))
d = abs(a*x + b*y - b) / math.sqrt(a**2 + b**2)
if d < r:
    print("Duong thang cat hoac nam trong duong tron")
elif d == r:
    print("Duong thang tiep xuc duong tron")
elif d > r:
    print("Duong thang nam ngoai duong tron")