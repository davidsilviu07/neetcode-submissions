class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stiva = []
        rez = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stiva and temperatures[stiva[-1]] < temperatures[i]:
                j = stiva.pop()
                rez[j] = i - j
            stiva.append(i)
        return rez