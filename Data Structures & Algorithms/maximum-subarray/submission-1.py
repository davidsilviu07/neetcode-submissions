class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best=0
        sum=0
        i=0
        if max(nums)<0:
            return max(nums)
        while i<len(nums):
            sum=sum+nums[i]
            if sum>best:
                best=sum
            if sum<0:
                sum=0
            i=i+1
        return best