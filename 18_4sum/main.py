# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
   

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Given an array nums of n integers, return an array of all the
        unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
        0 <= a, b, c, d < n
        a, b, c, and d are distinct.
        nums[a] + nums[b] + nums[c] + nums[d] == target
        You may return the answer in any order.        
        """
        a = []
        print("Nums: ", (nums))
        print("Target: ", (target))
        
        counter = 0
        while True:
            print("This loop will run forever!")
            counter += 1
            a=[]
            for range(len(nums)):
                s
                
            if counter == 5:
                break
        
        for i in range(len(nums)):
            if nums[i] + nums[-i] == 10:
                
                print("Deu Zero.")
            else:
                print("Não Deu Zero.")



result = Solution()

result = result.fourSum(nums = [1,0,-1,0,-2,2], target = 0)