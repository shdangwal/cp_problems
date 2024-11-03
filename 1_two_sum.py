class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for ind, num in enumerate(nums):
            comp = target - num
            if num in d:
                return [ind, d[num]]
            else:
                d[comp] = ind
