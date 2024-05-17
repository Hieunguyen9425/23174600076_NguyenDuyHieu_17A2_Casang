def printArmstrong():
    number = int(input("Nhập số bất kì: "))
    digit_sum = sum(int(digit) ** 3 for digit in str(number))
    if digit_sum == number:
        print(f"Số {number} là số Armstrong")
    else:
        print(f"Số {number} không là số Armstrong")
printArmstrong()