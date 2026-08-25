class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            seen = []
            count = 0
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                seen.append(s[j])
                count += 1
            longest = max(count,longest)
        return longest