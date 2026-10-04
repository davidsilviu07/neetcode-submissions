class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=0
        l=len(s)-1
        while r<l:
            if(s[r].isalnum() and s[l].isalnum()):
                if s[r].lower() != s[l].lower():
                    return False
                else:
                     r,l=r+1,l-1
            elif(not s[r].isalnum()):
                r=r+1    
            elif(not s[l].isalnum()):
                l=l-1     
        
        return True