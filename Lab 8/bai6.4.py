number = [2, 3, 4, 5, 6, 7, 8]
def cubic_number(number):
    return number ** 3
cubic_numbers = map(cubic_number, filter(lambda x: x % 2 == 0, number))
cubic_numbers_list = list(cubic_numbers)
print(cubic_numbers_list)
