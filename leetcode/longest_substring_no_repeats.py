class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxm = 0

        for i in range(len(s)):
            set1 = set()
            for j in range(i, len(s)):
                if(s[j] in set1):
                    break;
                else:
                    set1.add(s[j])
                    if(len(set1) > maxm):
                        maxm = len(set1)

        return maxm
