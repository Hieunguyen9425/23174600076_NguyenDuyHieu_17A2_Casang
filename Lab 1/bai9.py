mx,my = map(int, input("Nhap toa do M(Cach nhau bang khoang trong) : ").split())
nx,ny = map(int, input("Nhap toa do N(Cach nhau bang khoang trong) : ").split())
px,py = map(int, input("Nhap toa do P(Cach nhau bang khoang trong) : ").split())
qx,qy = map(int, input("Nhap toa do Q(Cach nhau bang khoang trong) : ").split())
mn = ((mx+nx)/2, (my+ny)/2)
np = ((nx+px)/2, (ny+py)/2)
pq = ((px+qx)/2, (py+qy)/2)
mq = ((mx+qx)/2, (my+qy)/2)
print(f"Trung diem MN la {mn}\nTrung diem NP la {np}\nTrung diem PQ la {pq}\nTrung diem MQ la {mq}")
