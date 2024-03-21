import math
e = math.e
x,z = map(float, input("Nhap x,z(Cach nhau bang khoang trong) : ").split())
tu = (x**2)*math.sin(z) + math.sqrt(abs(x)) #Tinh tu so
mau = math.log(z) + math.pow(e, x-1) #Tinh mau so
fxz = (tu/mau) + math.atan(x*z)
print(f"fxz = {fxz:.2f}")
