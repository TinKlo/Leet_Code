import logger
from tqdm import tqdm

logger_instance = logger.setup_logger()

num = [2, 7, 11,9,21, 15, 10, 15, 5,0]
target = 20

class Solution_1:
    def __init__(self):
        logger_instance.info('Class Called')

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a = []
        logger_instance.info('Function Called')
        logger_instance.debug('Running...')
        for i in tqdm(range(len(num)-1)):
            logger_instance.info(i)
            for j in range(i+1,len(nums)):
                logger_instance.info(j)
                if num[i] + num[j] == target:
                    
                    logger_instance.info(f"Answer: {[i,j]}")
                    return([i,j])
        logger_instance.info(f"Answer: {a}")

result = Solution_1()
result.twoSum(num, target)
