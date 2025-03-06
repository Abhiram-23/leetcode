class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        a = []
        b = 0
        for i in grid:
            a += i
        b += sum(a)
        c = sum(list(set(a)))
        rep = b-c
        a = sorted(list(set(a)))
        miss = 1
        for i in range(len(a)):
            if miss != a[i]:
                break
            miss += 1
        return [rep,miss]