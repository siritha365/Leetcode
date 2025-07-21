class Solution:
    def isThree(self, n: int) -> bool:
        count=1
        t=n//2
        for i in range(1,t+1):
            if n%i==0:
                count=count+1
        if count==3:
            return True
        else:
             return False
        
