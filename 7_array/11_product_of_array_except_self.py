from pip._vendor.typing_extensions import List


class Solution711:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        multiply = 1
        for i in range(len(nums)):
            result[i] = multiply
            multiply *= nums[i]

        multiply = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= multiply
            multiply *= nums[i]

        return result


s = Solution711()
# [24,12,8,6]
nums1 = [1, 2, 3, 4]
print(s.productExceptSelf(nums1))
# [0,0,9,0,0]
nums2 = [-1, 1, 0, -3, 3]
print(s.productExceptSelf(nums2))
