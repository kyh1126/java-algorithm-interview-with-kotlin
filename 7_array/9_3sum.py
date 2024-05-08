from pip._vendor.typing_extensions import List


class Solution79:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                # 합이 0보다 작다면 왼쪽 포인터 이동
                if sum < 0:
                    left += 1
                # 합이 0보다 크다면 오른쪽 포인터 이동
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    # 중복된 값 건너뛰기, 이 처리를 하지 않으면 같은 정답이 두 번 나올 수 있다.
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # 정답이 나왔으므로 투 포인터 모두 한 칸씩 이동.
                    left += 1
                    right -= 1

        return results


s = Solution79()
# [[-1, -1, 2], [-1, 0, 1]]
nums1 = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums1))
# []
nums2 = [0, 1, 1]
print(s.threeSum(nums2))
# [[0,0,0]]
nums3 = [0, 0, 0]
print(s.threeSum(nums3))
