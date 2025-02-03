class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        inc = 0
        cinc = 1
        dec = 0
        cdec = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cinc += 1
            else:
                cinc = 1
            if nums[i] < nums[i-1]:
                cdec += 1
            else:
                cdec = 1
            inc = max(cinc,inc)
            dec = max(dec,cdec)
        return max(inc,dec)