m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
if m != n:
    print("Ma trận vuông phải có cùng số hàng và cột")
else:
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            a = int(input(f"Nhập giá trị ở vị trí [{i}, {j}]: "))
            row.append(a)
        matrix.append(row)
    print("Ma trận đã nhập:")
    for row in matrix:
        print(row)

    check = True
    for i in range(m):
        for j in range(i, n):
            if matrix[i][j] != matrix[j][i]:
                check = False
                break
        if not check:
            break
    if check:
        print("Ma trận là ma trận đối xứng")
    else:
        print("Ma trận không phải là ma trận đối xứng")