import logger
from tqdm import tqdm

logger_instance = logger.setup_logger()


class Solution_1:
    def __init__(self):
        logger_instance.info('Class Called')

    def twoSum_brute(self, nums: list[int], target: int) -> list[int]:
        a = []
        logger_instance.info('Function Called')
        logger_instance.debug('Running...')
        for i in range(len(nums)):
            logger_instance.debug(f'Running i: { i }')
            for j in range(i+1,len(nums)):
                logger_instance.debug(f'Running j: { j }')
                if (nums[i]+nums[j])!=target:
                    continue
                else:
                    a.append(i)
                    a.append(j)
                    print(a)
                    logger_instance.debug(f'result { a }')
                    break
    def twoSum_mem(self, nums: list[int], target: int) -> list[int]:

        logger_instance.info('Function twoSum_mem Called')
        logger_instance.debug('Running...')

        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in seen:
                logger_instance.info(f"{ [seen[remaining]+1, i+1] }")
                return [seen[remaining]+1, i+1]
            else:
                seen[value] = 1


        n = len(nums)
        logger_instance.info(f'Len: {n}')
        for i in range(n):
            print(nums[i])
            numMap[nums[i]] = i
            logger_instance.info(f'i: {i}')
            logger_instance.info(f'numMap: {numMap}')
        for i in range(len(nums)):
            print(f"Target: {target}")
            d = (-i+target)
            print(f" Value of iteration: {nums[i]}")
            print(f"{d}")

    def twoSum_self(self, nums: list[int], target: int) -> list[int]:
        logger_instance.info(f"Function twoSum_self Called")
        logger_instance.info(f"Input Numbers: {nums}, Target: {target}")
        a = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]) == target:
                    print("This is Result: ")
                    print([nums[i],nums[j]])
                    break
                else:
                    continue
    def twoSum_self(self, nums: list[int], target: int) -> list[int]:
    
result = Solution_1()
# result.twoSum_brute(nums=[2, 7, 11,9], target=9)
result.twoSum_self(nums=[3,2,4],target=6)

