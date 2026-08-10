class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = []
        nums.sort()
        count = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                l.append([nums[i-1],count])
                count = 1
            else:
                count = count + 1
        l.append([nums[-1], count])
        sorted_data = sorted(l, key=lambda x: x[1], reverse=True)
        result = [sorted_data[x][0] for x in range(k)]
        return result 