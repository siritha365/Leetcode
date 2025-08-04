class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s=sum(nums)
        missing_num=int(n*(n+1)/2-s)
        return missing_num
        
