class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26
        for cha in s:
            arr[ord(cha) - 97] += 1
        for cha in t:
            arr[ord(cha) - 97] -= 1 
        for i in arr :
            if i != 0:
                return False
        return True