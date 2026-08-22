# import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict, t_dict = {}, {}
        for x in range(len(s)):
            if s[x] not in s_dict:
                s_dict[s[x]] = 1
            else:
                s_dict[s[x]] += 1
        # for x in range(len(t)):
            if t[x] not in t_dict:
                t_dict[t[x]] = 1
            else:
                t_dict[t[x]] += 1
        return s_dict == t_dict