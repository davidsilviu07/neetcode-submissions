class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        P=[1]
        P2=[1]
        for i,x in enumerate(nums):
            P.append(P[-1]*x)
        
        for i in range(len(nums)-1,-1,-1):
             P2.append(P2[-1]*nums[i])
        Array=[1]*len(nums)
        for i,x in enumerate(nums):
            Array[i]=P[i]*P2[len(nums)-1-i]
        return Array



