def is_odd(number):
    return number % 2 == 0
def filter_odd_numbers(numbers):
    odd_numbers = list(filter(is_odd, numbers))
    return odd_numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter_odd_numbers(numbers)
print(f"Các số chẵn trong danh sách là:  {odd_numbers}")