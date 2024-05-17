number = [2, 3, 4, 5, 6, 7, 8]
def square_number(number):
    return number ** 2
square_number = map(square_number, filter(lambda x: x % 2 != 0, number))
square_number_list = list(square_number)
print(square_number_list)