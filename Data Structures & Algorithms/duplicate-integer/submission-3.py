class Solution:
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     if len(set(nums)) != len(nums):
    #         return True
    #     else:
    #         return False 

    # other method

    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_values = set()
        for x in nums:
            if x in unique_values:
                return True
            else:
                unique_values.add(x)
        return False