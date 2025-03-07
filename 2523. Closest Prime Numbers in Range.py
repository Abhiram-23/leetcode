from math import sqrt
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(n):
            if n <= 1:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True

        op = []
        mini = 1000000
        res = []
        for i in range(left,right+1):
            if is_prime(i):
                if len(op) > 0:
                    b = op.pop()
                    op.append(i)
                    if i-b<mini:
                        mini = i-b
                        res = [b,i]
                    if mini <= 2:
                        return res
                op.append(i)
        if len(op) <2:
            return [-1,-1]
        return res