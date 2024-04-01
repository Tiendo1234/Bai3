n = int(input("Nhap n: "))
mang = [int(input("Nhap so: ")) for i in range(n)]
max_mang = max(mang)
scn_arr = []


class bai6:

    def __init__(self, n, mang):
        self.n = n
        self.mang = mang

    def scn_max(self):
        for i in mang:
            if i == max_mang:
                continue
            else:
                scn_arr.append(i)
        scn_arr.sort(reverse=True)
        return scn_arr[0]

    def ucln(self):
        dem_uc = 0
        for i in mang:
            if max_mang % i == 0:
                dem_uc += 1
        if dem_uc == n:
            print(f"Uoc chung lon nhat la: {min(mang)}")
        else:
            print(f"Uoc chung lon nhat la 1")

    def bcnn(self):
        dem_bc = 0
        for i in mang:
            if i % min(mang) == 0:
                dem_bc += 1
            else:
                break
        if dem_bc == n:
            print(f"Boi chung nho nhat la: {(max_mang*self.scn_max())}")
        else:
            for i in mang:
                dem_bc *= i
            print(f"Boi chung nho nhat la: {dem_bc}")


p = bai6(n, mang)
p.scn_max()
p.ucln()
p.bcnn()
