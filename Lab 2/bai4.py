diem = float(input("Nhap diem : "))
if 0 <= diem < 5:
    print("Điểm kém")
elif 5 <= diem < 7:
    print("Điểm trung bình")
elif 7 <= diem < 8.5:
    print("Điểm khá")
else:
    print("Điểm tốt")