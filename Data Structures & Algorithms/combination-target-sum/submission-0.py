class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        rez = []
        curent = []

        def bt(start, suma):
            if suma == target:
                rez.append(curent[:])
                return
            if suma > target:
                return
            for i in range(start, len(candidates)):
                curent.append(candidates[i])
                bt(i, suma + candidates[i])
                curent.pop()

        bt(0, 0)
        return rez