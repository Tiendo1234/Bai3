x = int(input("Nhap x: "))
n = int(input("Nhap n: "))
mang = [int(input("Nhap so: ")) for i in range(n)]


class bai4:
    def __init__(self, x, n, mang):
        self.n = n
        self.x = x
        self.mang = mang

    def dem_x(self):
        dem = 0
        for i in range(len(mang)):
            if mang[i] == x:
                dem += 1
                mang[i] = str(mang[i]) + "x"
            else:
                continue
        print(f"Co {dem} bang x")
        print(mang)


p = bai4(x, n, mang)
p.dem_x()
