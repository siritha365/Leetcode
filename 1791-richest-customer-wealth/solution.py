class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum=0
        m=len(accounts)
        for i in range(m):
             rowsum=sum(accounts[i])
             if rowsum>max_sum:
                 max_sum=rowsum
        return max_sum    
        
