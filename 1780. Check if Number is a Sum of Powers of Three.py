class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1:
            k = n % 3
            if k == 2:
                return False
            n = n//3
        return True    