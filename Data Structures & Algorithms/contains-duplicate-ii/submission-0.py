class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        fereastra = set()
        for i in range(len(nums)):
            if nums[i] in fereastra:
                return True
            fereastra.add(nums[i])
            if len(fereastra)>k:
                fereastra.discard(nums[i-k])

        return False