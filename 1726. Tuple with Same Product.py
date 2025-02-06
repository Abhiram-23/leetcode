class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        op = 0
        a = {}
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                b = nums[i]*nums[j]
                if b in a:
                    a[b] += 1
                else:
                    a[b] = 1
        for i in a:
            if a[i] >= 2:
                op += 4*(a[i])*(a[i]-1)
        return op