class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in counter:
                return [counter[difference],i]
            else:
                counter[nums[i]]= i
