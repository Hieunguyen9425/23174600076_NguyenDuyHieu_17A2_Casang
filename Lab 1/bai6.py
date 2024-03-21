import math
ax = float(input("Nhap hoanh do vector a : "))
ay = float(input("Nhap tung do vector a : "))
bx = float(input("Nhap hoanh do vector b : "))
by = float(input("Nhap hoanh do vector b : "))
#Tong hieu 2  vector
tongabx = ax + bx
tongaby = ay + by
hieuabx = ax - bx
hieuaby = ay - by
print(f"Tong 2 vector a & b la : ({tongabx},{tongaby})")
print(f"Hieu 2 vector a & b la : ({hieuabx},{hieuaby})")

#Do dai 2 vector
do_dai_a = math.sqrt(ax**2 + ay**2)
do_dai_b = math.sqrt(bx**2 + by**2)
print(f"Do dai vector a la : {do_dai_a}")
print(f"Do dai vector b la : {do_dai_b}")

#Cosin goc hop giua 2 vector
cosinab = (ax*bx + ay*by) / (do_dai_a * do_dai_b)
print(f"Cosin goc xen giua 2 vector a & b la : {cosinab:.2f}")