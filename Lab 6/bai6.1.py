m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
matrix = []
for i in range(m):
    row = []
    for j in range(n):
        a = int(input(f"Nhập giá trị ở vị trí [{i}, {j}]: "))
        row.append(a)
    matrix.append(row)

sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        sum += matrix[i][j]
print(f"Tổng của các phần tử của ma trận là: {sum}")

transpose_matrix = [[matrix[i][j] for i in range(m)] for j in range(n)]

print("Ma trận chuyển vị là:")
for row in transpose_matrix:
    print(row)