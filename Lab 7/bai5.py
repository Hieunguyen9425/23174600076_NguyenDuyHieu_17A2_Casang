kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

hoa_don = {}

tong_tien = 0
for mat_hang in kho:
    so_luong = kho[mat_hang]
    don_gia = gia_tien[mat_hang]
    tien_hang = so_luong * don_gia
    hoa_don[mat_hang] = {
        "so_luong": so_luong,
        "don_gia": don_gia,
        "tien_hang": tien_hang
    }
    tong_tien += tien_hang

print("Hóa đơn mua hàng:")
for mat_hang, thong_tin in hoa_don.items():
    print(f"Mặt hàng: {mat_hang}")
    print(f"Số lượng: {thong_tin['so_luong']}")
    print(f"Đơn giá: {thong_tin['don_gia']}")
    print(f"Số tiền của mặt hàng: {thong_tin['tien_hang']}")
    print()

print(f"Tổng số tiền của hóa đơn: {tong_tien}")

print("\nSố lượng của các mặt hàng trong kho sau khi mua:")
for mat_hang, so_luong in kho.items():
    print(f"{mat_hang}: {so_luong}")
