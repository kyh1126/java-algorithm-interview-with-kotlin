from pip._vendor.typing_extensions import List


class Solution77:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for idx, n in enumerate(nums):
            if (target - n) in dic:
                return [dic[target - n], idx]
            dic[n] = idx


s = Solution77()
# [0, 1]
nums1 = [2, 7, 11, 15]
target1 = 9
print(s.twoSum(nums1, target1))
# [1, 2]
nums2 = [3, 2, 4]
target2 = 6
print(s.twoSum(nums2, target2))
# [0, 1]
nums3 = [3, 3]
target3 = 6
print(s.twoSum(nums3, target3))
