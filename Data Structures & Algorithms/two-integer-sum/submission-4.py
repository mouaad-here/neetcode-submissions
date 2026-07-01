class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force

        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # Sorting the list and using 2 pointers

        # nums_sorted = sorted(nums)

        # l = 0
        # r = len(nums) - 1
        # while l < r:
        #     if nums_sorted[l] + nums_sorted[r] < target:
        #         l += 1
        #     elif nums_sorted[l] + nums_sorted[r] > target:
        #         r -= 1
        #     else:
        #         return [nums.index(nums_sorted[l]), nums.index(nums_sorted[r])]
        seen  = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            else:
                seen[nums[i]] = i
            
