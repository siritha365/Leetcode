class Solution:
    def countDigits(self, num: int)->int:
        count=0
        n=num
        while num>0:
            i=num%10
            num//=10
            if n%i==0:
                count+=1
        return count
        
        
