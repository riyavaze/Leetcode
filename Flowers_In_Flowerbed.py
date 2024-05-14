class Solution:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        # If there are no flowers to plant, return True immediately.
        if n == 0:
            return True
        
        # Iterate through each slot in the flowerbed.
        for i in range(len(flowerbed)):
            # Check if the current slot is empty and the adjacent slots (if they exist) are also empty.
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                # Plant a flower in the current slot.
                flowerbed[i] = 1
                # Decrease the count of flowers needed to be planted.
                n -= 1
                # If no more flowers need to be planted, return True.
                if n == 0:
                    return True
        # If the loop finishes and not all flowers have been planted, return False.
        return False
