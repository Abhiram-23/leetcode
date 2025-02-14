class ProductOfNumbers:

    def __init__(self):
        self.pro = 1
        self.arr = []

    def add(self, num: int) -> None:
        if num:
            self.pro *= num
            self.arr.append(self.pro)
        else:
            self.arr = []
            self.pro = 1

    def getProduct(self, k: int) -> int:
        if len(self.arr) < k:
            return 0
        elif len(self.arr) == k:
            return self.pro
        else:
            return self.pro//self.arr[-k-1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)