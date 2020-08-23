from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=0
        for i in range(0,len(height)-1):
            leftSide=height[i]
            possibleMaxArea= leftSide*(len(height)-i)
            if(possibleMaxArea<maxArea):
                continue
            for j in range(i+1,len(height)):
                rightSide=height[j]
                side=0;
                if(leftSide<rightSide):
                    side=leftSide
                else:
                    side=rightSide
                bottomSide=j-i;
                area=bottomSide * side;
                if(maxArea < area):
                    maxArea=area
        return maxArea
instance = Solution()
output = instance.maxArea([1,8,6,2,5,4,8,3,7]);
print(output)