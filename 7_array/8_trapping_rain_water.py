from pip._vendor.typing_extensions import List


class Solution78:
    def trap(self, height: List[int]) -> int:
        volume = 0
        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            leftMax = max(height[left], leftMax)
            rightMax = max(height[right], rightMax)

            if leftMax < rightMax:
                volume += leftMax - height[left]
                left += 1
            else:
                volume += rightMax - height[right]
                right -= 1

        return volume


s = Solution78()
# 6
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(s.trap(height1))
# 9
height2 = [4, 2, 0, 3, 2, 5]
print(s.trap(height2))
