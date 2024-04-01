n = int(input("Nhap n: "))
my_dict = {}
for i in range(n):
    n = int(input("Nhap key: "))
    val = input("Nhap ten: ")
    my_dict.update({n: val})


class bai7:
    def __init__(self, n, my_dict):
        self.n = n
        self.my_dict = my_dict

    def tim_ten(self):
        k = int(input("Nhap key"))
        for i in my_dict:
            if i == k:
                return my_dict[i]
            else:
                continue

    def tim_key(self):
        t = input("Nhap ten: ")
        for i in my_dict:
            if my_dict[i] == t:
                return i
            else:
                continue


p = bai7(n, my_dict)
print(p.tim_ten())
print(p.tim_key())
