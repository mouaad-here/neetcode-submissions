class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        count = 1
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                l.append([nums[i-1], count])
                count = 1
            else:
                count += 1
        l.append([nums[-1], count])
        l_sorted = sorted(l, key=lambda x: x[1], reverse=True)
        return [x[0] for x in l_sorted[:k]]