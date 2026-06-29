class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum=sum(ord(i) for i in s)
        t_sum=sum(ord(i) for i in t)
        return chr(t_sum-s_sum)
        
        
