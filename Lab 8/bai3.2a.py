def printArmstrong():
    for number in range(1, 1000):
        digit_sum = sum(int(digit) ** 3 for digit in str(number))
        if digit_sum == number:
            print(number)
printArmstrong()