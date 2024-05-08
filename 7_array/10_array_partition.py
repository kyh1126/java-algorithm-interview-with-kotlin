from pip._vendor.typing_extensions import List


class Solution710:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0

        for i in range(0, len(nums), 2):
            result += min(nums[i], nums[i + 1])

        return result


s = Solution710()
# 4
nums1 = [1, 4, 3, 2]
print(s.arrayPairSum(nums1))
# 9
nums2 = [6, 2, 6, 5, 1, 2]
print(s.arrayPairSum(nums2))
