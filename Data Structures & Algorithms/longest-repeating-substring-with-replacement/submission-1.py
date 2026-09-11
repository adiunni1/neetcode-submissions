class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        result = 0 
        count = {}

        while left <= right and right < len(s):
            count[s[right]] = 1 + count.get(s[right], 0)
            windowSize = right - left + 1
            if windowSize - max(count.values()) <= k:
                result = max(result, windowSize)
            else:
                count[s[left]] -= 1
                left += 1
            right += 1
            
        return result