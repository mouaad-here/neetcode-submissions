class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        out = []
        for i in range(len(strs)):
            if strs[i] not in seen:

                group = [strs[i]]
                seen.add(strs[i])
                for j in range(i + 1, len(strs)):
                    if sorted(strs[i]) == sorted(strs[j]):
                        group.append(strs[j])
                        seen.add(strs[j])
                out.append(group)
        
        return out