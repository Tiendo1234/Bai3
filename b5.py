mang = [input("Nhap chu cai: ") for i in range(4)]


class bai5:
    def __init__(self, mang):
        self.mang = mang

    def my_tuple(self):
        arr = []
        for i in mang:
            if i.isupper():
                arr.append(i)
            else:
                continue
        return tuple(arr)


p = bai5(mang)
print(p.my_tuple())
