def sum_of_divisors(n):
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum

def are_amicable(num1, num2):
    if sum_of_divisors(num1) == num2 and sum_of_divisors(num2) == num1:
        return True
    else:
        return False

num1, num2 = map(int, input("Nhập 2 số bất kì: ").split())

if are_amicable(num1, num2):
    print(f"{num1} và {num2} là một cặp số amicable.")
else:
    print(f"{num1} và {num2} không phải là một cặp số amicable.")
