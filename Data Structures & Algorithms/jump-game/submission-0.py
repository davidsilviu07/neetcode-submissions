class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lun = len(nums) - 1
        index = 0
        while index < lun and nums[index] != 0:
            if index + nums[index] >= lun:
                return True
            best = index
            best_reach = index + nums[index]
            for j in range(index + 1, index + nums[index] + 1):
                if j + nums[j] > best_reach:
                    best_reach = j + nums[j]
                    best = j
            if best == index:
                return False
            index = best
        return index >= lun