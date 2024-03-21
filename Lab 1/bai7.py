a1, b1, c1 = map(int, input("Nhap he so a1, b1, c1 (Cach nhau bang khoang trong): ").split())
a2, b2, c2 = map(int, input("Nhap he so a2, b2, c2 (Cach nhau bang khoang trong): ").split())
print(f"He phuong trinh da nhap : {a1}x + {b1}y = {c1} \n{' '*26}{a2}x + {b2}y = {c2}")

#Tinh x,y bang phuong phap cramer
y = (c2*a1 - c1*a2) / (b2*a1 - b1*a2)
x = (c1 - b1*y) / a1
print(f"Gia tri cua x la: {x:.2f}")
print(f"Gia tri cua y la: {y:.2f}")
