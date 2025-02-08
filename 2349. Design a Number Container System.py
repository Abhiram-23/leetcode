class NumberContainers:

    def __init__(self):
        self.ind = {}
        self.num = {}


    def change(self, index: int, number: int) -> None:
        if index in self.ind:
            prev_number = self.ind[index]
            if prev_number in self.num:
                self.num[prev_number].discard(index)  
                if not self.num[prev_number]: 
                    del self.num[prev_number]

        self.ind[index] = number 
        if number not in self.num:
            self.num[number] = SortedSet()
        self.num[number].add(index)

    def find(self, number: int) -> int:
        if number in self.num and self.num[number]:
            return self.num[number][0]
        return -1



# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)