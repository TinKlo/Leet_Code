# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps


import random

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        prevPrev = 1
        prev = 2
        current = 0

        for step in range(3, n+1):
            # Calculate Number of Ways to Reach Current Step
            current = prevPrev + prev
            # Update Pointers for Next Step
            prevPrev = prev
            prev = current
        print(current)    
        return current
        
result = Solution()
# n = random.randint(3, 9)

result.climbStairs(n=4)