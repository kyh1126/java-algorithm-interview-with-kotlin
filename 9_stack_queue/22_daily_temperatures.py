from pip._vendor.typing_extensions import List


class Solution922:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last = stack.pop()
                result[last] = i - last
            stack.append(i)

        return result


s = Solution922()
# [1,1,4,2,1,1,0,0]
s1 = [73, 74, 75, 71, 69, 72, 76, 73]
print(s.dailyTemperatures(s1))
# [1,1,1,0]
s2 = [30, 40, 50, 60]
# print(s.dailyTemperatures(s2))
# [1,1,0]
s3 = [30, 60, 90]
# print(s.dailyTemperatures(s3))
