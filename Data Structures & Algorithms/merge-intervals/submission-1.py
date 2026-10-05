class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        rez=[intervals[0]]
        for i in range(1,len(intervals)):
                if rez[-1][1]>=intervals[i][0]:
                    if rez[-1][1]<intervals[i][1]:
                        rez[-1][1]=intervals[i][1]
                else:
                    rez.append(intervals[i])
        return rez
