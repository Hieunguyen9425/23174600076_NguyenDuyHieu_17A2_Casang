a1, b1 = map(float, input("Nhap he so goc va he so tu do cua duong thang thu nhat: ").split())
a2, b2 = map(float, input("Nhap he so goc va he so tu do cua duong thang thu hai: ").split())

if a1 * a2 == -1:
    print("Hai duong thang vuong goc")
elif a1 == a2 and b1 != b2:
    print("Hai duong thang song song")
elif a1 != a2:
    print("Hai duong thang cat nhau")

