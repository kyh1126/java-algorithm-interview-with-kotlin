from pip._vendor.typing_extensions import List


class Solution712:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buyIdx, sellIdx, minIdx, answer = 0, 1, 0, 0

        while sellIdx < len(prices):
            if prices[buyIdx] > prices[minIdx]:
                buyIdx = minIdx
            answer = max(answer, prices[sellIdx] - prices[buyIdx])

            if prices[sellIdx] < prices[minIdx]:
                minIdx = sellIdx
            sellIdx += 1

        return answer


s = Solution712()
# 5
prices1 = [7, 1, 5, 3, 6, 4]
print(s.maxProfit(prices1))
# 0
prices2 = [7, 6, 4, 3, 1]
print(s.maxProfit(prices2))
