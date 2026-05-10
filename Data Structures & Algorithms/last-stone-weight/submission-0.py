class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        while len(stones) > 1:

            y = max(stones)
            stones.remove(y)

            x = max(stones)
            stones.remove(x)

            if y != x:
                stones.append(y - x)

        return stones[0] if stones else 0
       
        

            
            
        