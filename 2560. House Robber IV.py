
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # Binary search for the minimum capability
        def canRob(capability):
            count, i = 0, 0
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 1  # Skip adjacent house
                i += 1  # Move to next house
            return count >= k
        
        # Perform binary search on the capability
        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if canRob(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
