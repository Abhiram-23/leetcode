class Solution:
    def minOperations(self, nums: List[int]) -> int:
        co = 0
        n = len(nums)
        for i in range(n-2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                co += 1
        return co if (nums[n-2]==1 and nums[n-1]==1) else -1