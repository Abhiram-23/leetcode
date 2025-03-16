import math
class Solution:
    def repairCars(self, ranks, cars) -> int:
        maxi = max(ranks)*(cars**2)
        low = 0
        high = maxi+1
        def check(maxtime):
            count = 0
            for i in ranks:
                b = maxtime/i
                count += int(math.sqrt(b))
                if count >= cars:
                    return True
            return False
        minop = high
        while low <= high:
            mid = (low+high)//2
            if check(mid):
                minop = min(minop,mid)
                high = mid-1
            else:
                low = mid+1
        return minop