so_chu_so = 0
so = int(input("Nhap so nguyen : "))
so_con_lai = so
while so_con_lai > 0:
    so_con_lai //= 10
    so_chu_so += 1
print("So chu so da nhap:", so_chu_so)