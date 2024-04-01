n = int(input("Nhap n: "))
mang1 = [int(input("Nhap so mang 1: ")) for i in range(n)]
mang2 = [int(input("Nhap so mang 2: ")) for i in range(n)]
mydict = {}


class bai1:
    def __init__(self, n, mang1, mang2):
        self.n = n
        self.mang1 = mang1
        self.mang2 = mang2

    def my_dict(self):
        for i in range(self.n):
            mydict[self.mang1[i]] = self.mang2[i]
        return mydict


p = bai1(n, mang1, mang2)
print(p.my_dict())
