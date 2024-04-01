n = int(input("Nhap n: "))
mang = [int(input("Nhap so: ")) for i in range(n)]


class bai3:
    mang_am = []
    mang_duong = []
    dem_am = 0
    dem_duong = 0

    def __init__(self, n, mang):
        self.n = n
        self.mang = mang

    def dem(self):
        for i in mang:
            if i < 0:
                self.dem_am += 1
                self.mang_am.append(i)
            else:
                self.dem_duong += 1
                self.mang_duong.append(i)
        print(f"Co {self.dem_am} so am")
        print(f"Co {self.dem_duong} so duong")

    def tbc(self):
        tong_am = 0
        tong_duong = 0
        for i in self.mang_am:
            tong_am += i
        for a in self.mang_duong:
            tong_duong += a
        print(f"Trung binh cong so am: {float(tong_am/self.dem_am)}")
        print(f"Trung binh cong so duong: {float(tong_duong/self.dem_duong)}")


p = bai3(n, mang)
p.dem()
p.tbc()
