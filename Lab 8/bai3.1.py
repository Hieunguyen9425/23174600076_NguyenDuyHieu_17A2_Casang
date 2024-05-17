def cubesum(number):
    sum_squared = 0
    while number > 0:
        digit = number % 10
        sum_squared += digit ** 2
        number //= 10
    return sum_squared
num = int(input("Nhập vào một số: "))
squared_sum = cubesum(num)
print("Tổng bình phương các chữ số trong số đó là:", squared_sum)