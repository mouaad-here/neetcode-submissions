from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #auto create an empty list for messing keys
        group = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            group[key].append(word)
        
        return list(group.values())