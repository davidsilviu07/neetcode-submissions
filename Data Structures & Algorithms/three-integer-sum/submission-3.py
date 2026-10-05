class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rez = []
        nums.sort()
        if nums[0] + nums[1] + nums[2] > 0:
            return []
        for l in range(len(nums) - 2):
            if l > 0 and nums[l] == nums[l - 1]:
                continue
            k = l + 1
            r = len(nums) - 1
            while k < r:
                s = nums[l] + nums[k] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    k += 1
                else:
                    rez.append([nums[l], nums[k], nums[r]])
                    k += 1
                    r -= 1
                    while k < r and nums[k] == nums[k - 1]:
                        k += 1
        return rez