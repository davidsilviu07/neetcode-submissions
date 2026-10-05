class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        list = []
        r = len(arr) - 1
        l = 0
        if x < arr[0]:
            list = arr[0:k]
            return list
        elif x > arr[-1]:
            list = arr[len(arr) - k:]
            return list
        else:
            while r - l + 1 > k:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    r = r - 1
                else:
                    l = l + 1
            list = arr[l:r + 1]
        return list