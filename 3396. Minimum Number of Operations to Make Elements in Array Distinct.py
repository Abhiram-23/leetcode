class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op = 0
        while len(nums) != len(set(nums)):
            if len(nums) >= 3:
                nums.pop(0)
                nums.pop(0)
                nums.pop(0)
            else:
                nums = []
            op += 1
        return op