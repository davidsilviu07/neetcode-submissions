class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        for i in range(len(strs[0])):
           for cuv in range(len(strs)-1):
              if(i>=len(strs[cuv+1]) or      
              
              strs[cuv][i]!=strs[cuv+1][i]):
                return strs[0][ :i]
        return strs[0]

