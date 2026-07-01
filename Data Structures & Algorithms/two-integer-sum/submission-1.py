class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        # Sorting the list and using 2 pointers

        nums.sort()

        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r += 1
            else:
                return [l, r]
