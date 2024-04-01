import math

n = int(input("Nhap n: "))


class bai8:
    def __init__(self, n):
        self.n = n

    def tinh_can(self):
        a = math.sqrt(n)
        return a

    def binh_phuong(self):
        a = n * n
        return a

    def kc(self):
        d1 = [int(input("Nhap a1, b1 lan luot la: ")) for i in range(2)]
        d2 = [int(input("Nhap a2, b2 lan luot la: ")) for i in range(2)]
        a = math.sqrt((d2[0] - d1[0]) + (d2[1] - d1[0]))
        return a

    def kiem_tra(self):
        canh = [int(input("Nhap canh a, b, c lan luot la: ")) for i in range(3)]
        arr = []
        if (
            abs(canh[1] - canh[2]) < canh[0]
            or canh[0] > abs(canh[1] + canh[2])
            or canh[0] == max(canh)
        ):
            print("a,b,c co the tao thanh mot tam giac")
        else:
            print("a,b,c khong tao thanh 1 tam giac duoc")

    def cv_s(self):
        cv = 0
        for i in arr:
            cv += i
        p = cv / 2
        s = math.sqrt(p * (p - arr[0]) * (p - arr[1]) * (p - arr[2]))
        print(f"Chu vi hinh tam giac la: {cv}")
        print(f"Dien tich hinh tam giac la: {s}")


p = bai8(n)
print(p.tinh_can())
print(p.binh_phuong())
print(p.kc())
p.kiem_tra()
p.cv_s()
