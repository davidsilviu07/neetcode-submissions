class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suma=sum(nums)
        P=[0]
        for i,x in enumerate(nums):
            P.append(P[-1]+x)
            if suma-P[i]-x==P[i]:

                return i
        return -1
