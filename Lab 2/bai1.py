a,b = map(int, input("Nhap he so a,b : ").split())
if a != 0 :
    nghiem = -b/a
    print(f"Ngiem cua phuong trinh la {nghiem}")
elif a == 0 and b == 0 :
    print("Phuong trinh co vo so nghiem")
elif a == 0 and b != 0 :
    print("Phuong trinh da cho vo nghiem")
