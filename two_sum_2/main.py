class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        print(nums)
        print(target)
        a = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                
                b = nums[i]+nums[j]
                if b == target:                  
                    s = list[nums[i],nums[j]]
                    return s
                    break
                else:
                    continue
                #print(j)
                #print(i)
            
            
        
result = Solution()

result.twoSum(nums=[2, 7, 11, 15], target = 9)
