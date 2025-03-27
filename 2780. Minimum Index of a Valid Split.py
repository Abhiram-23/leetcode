class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dic = {}
        leng = len(nums)
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        leftdic = {}
        for i in range(len(nums)):
            if nums[i] in leftdic:
                leftdic[nums[i]] += 1
            else:
                leftdic[nums[i]] = 1
            dic[nums[i]] -= 1
            if leftdic[nums[i]]*2>(i+1) and dic[nums[i]]*2 >(leng-i-1):
                return i
        return -1