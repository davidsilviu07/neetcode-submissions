class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        rez = 0
        ultim_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < ultim_end:
                rez += 1
            else:
                ultim_end = intervals[i][1]
        return rez