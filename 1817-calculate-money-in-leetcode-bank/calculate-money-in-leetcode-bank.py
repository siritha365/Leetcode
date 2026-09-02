class Solution:
    def totalMoney(self, n: int) -> int:
        result = 0
        monday = 1

        while n > 0:
            days = min(n, 7)

            for day in range(days):
                result += monday + day

            n -= days
            monday += 1

        return result     
        