class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxm = 0
        i = 0
        j = len(height)-1

        while i <= j:
            c_w = min(height[i], height[j]) * (j-i)

            if c_w > maxm:
                maxm = c_w

            if height[j] < height[i]:
                j -= 1
            else:
                i += 1

        return maxm
