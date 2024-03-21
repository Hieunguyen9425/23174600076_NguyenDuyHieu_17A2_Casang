a,b,c = map(int, input("Nhap 3 so nguyen duong : ").split())
if a < b < c or c < a < b:
    print(f"So lon thu 2 la {b}")
elif a < c < b or b < c < a:
    print(f"So lon thu 2 la {c}")
elif b < a < c or c < a < b:
    print(f"So lon thu 2 la {a}")