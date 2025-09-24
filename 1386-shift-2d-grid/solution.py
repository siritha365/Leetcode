class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        total=m*n
        k%=total
        a=[num for row in grid for num in row]
        a=a[-k:]+a[:-k]
        new_grid=[]
        for i in range(m):
           row_grid=a[i*n:(i+1)*n]
           new_grid.append(row_grid)
        return new_grid   
        
