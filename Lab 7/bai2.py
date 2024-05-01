f_list = []
d_list = []
c_list = []
b_list = []
a_list = []

for i in range(1, 11):
    names = input("Nhập tên sinh viên(Cách nhau bằng khoảng trống): ").split()
    grades = map(float, input("Nhập điểm số của sinh viên(Cách nhau bằng khoảng trống): ").split())

    names = list(names)
    
    j = 0
    for grade in grades:
        name = names[j]
        j += 1
        
        if grade < 4:
            f_list.append((name, grade))
        elif 4 <= grade < 5.5:
            d_list.append((name, grade))
        elif 5.5 <= grade < 7:
            c_list.append((name, grade))
        elif 7 <= grade < 8.5:
            b_list.append((name, grade))
        else:
            a_list.append((name, grade))

    statistic_f_list = len(f_list)
    statistic_d_list = len(d_list)
    statistic_c_list = len(c_list)
    statistic_b_list = len(b_list)
    statistic_a_list = len(a_list)
    
print(f"Danh sách sinh viên có điểm là F:{f_list}\nDanh sách sinh viên có điểm là D:{d_list}\nDanh sách sinh viên có điểm là C:{c_list}\nDanh sách sinh viên có điểm là B:{b_list}\nDanh sách sinh viên có điểm là A:{a_list}")
print(f"Số lượng sinh viên có điểm là F: {statistic_f_list}\nSố lượng sinh viên có điểm là D: {statistic_d_list}\nSố lượng sinh viên có điểm là C: {statistic_c_list}\nSố lượng sinh viên có điểm là B: {statistic_b_list}\nSố lượng sinh viên có điểm là A: {statistic_a_list}")