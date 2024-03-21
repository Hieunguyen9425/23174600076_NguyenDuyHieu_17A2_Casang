
weight = float(input("Nhap can nang : "))
height = float(input("Nhap chieu cao : "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Gầy")
elif 18.5 <= bmi < 24.9:
    print("Bình thường")
elif 24.9 <= bmi <29.9:
    print("Hơi béo")
else:
    print("Béo")