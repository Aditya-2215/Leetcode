class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                distance=(x-xCenter)**2+(y-yCenter)**2
                if distance<=radius**2:
                    return True
        return False
