import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        op = 0
        while True:
            if len(nums) >= 2:
                a = heapq.heappop(nums)
                b = heapq.heappop(nums)
                if min(a,b) < k:
                    c = ((min(a,b))*2 + max(a,b))
                    heapq.heappush(nums,c)
                    op += 1
                else:
                    break
            else:
                break
        return op