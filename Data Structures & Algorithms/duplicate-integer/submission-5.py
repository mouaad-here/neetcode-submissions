class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        else:
            return False 

    # other method

    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     unique_nums = set()
    #     for x in nums:
    #         if x in unique_values:
    #             return True
    #         else:
    #             unique_nums.add(x)
    #     return False

    # brute force

    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     for i in range(len(nums)-1):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] == nums[j]:
    #                 return True
    #     return False