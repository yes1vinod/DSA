from typing import List


class Solution:
    def minPathSum(self, grid):
        maxRow = len(grid)
        maxColumn = len(grid[0])
        newRow=[[0]*maxColumn]*maxRow
        i=0
        
        for rows in grid:
            newColumn=[]
            j=0
            for columns in rows:
                print("i >>" + str(i))
                print("j >>" + str(j))
                columnValue= columns
                if(i>0 and j>0):
                    
                    columnValue=columnValue+min(newRow[i][j-1],newRow[i-1][j])
                elif (i>0):
                    columnValue=columnValue+newRow[i-1][j]
                elif(j>0):
                    columnValue=columnValue+newRow[i][j-1]
                newRow[i][j]=columnValue
                j=j+1
            i=i+1
            # newRow.append(newColumn)
        print(newRow)
        return newRow[maxRow-1][maxColumn-1]

    

instance = Solution()
output = instance.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]);
