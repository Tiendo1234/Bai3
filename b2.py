n = int(input("Nhap n: "))
mang = [int(input("Nhap so: ")) for i in range(n)]
my_dict = {}


class bai2:
    def __init__(self, n, mang):
        self.n = n
        self.mang = mang

    def my_dict(self):
        for i in range(self.n):
            my_dict[self.mang[i]] = self.mang[i] ** 2
        return my_dict


p = bai2(n, mang)
print(p.my_dict())
