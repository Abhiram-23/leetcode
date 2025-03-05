class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        op = []
        z = []
        while i < len(nums):
            if i+1 < len(nums) and nums[i] != 0 and nums[i] == nums[i+1]:
                op.append(2*nums[i])
                z.append(0)
                i += 2
            elif nums[i] == 0:
                z.append(0)
                i+=1
            else:
                op.append(nums[i])
                i+=1
        return op+z