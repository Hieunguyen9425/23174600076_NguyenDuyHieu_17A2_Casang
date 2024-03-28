a, b = 0, 1
for _ in range(100):
    if a >= 100:
        break
    print(a, end=' ')
    a, b = b, a + b
