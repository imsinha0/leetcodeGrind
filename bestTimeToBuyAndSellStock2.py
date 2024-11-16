class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        totalProfit = 0

        for ind in range(len(prices)-1):
            if prices[ind+1] > prices[ind]:
                totalProfit += prices[ind+1] - prices[ind]

        return totalProfit





if __name__ == "__main__":
    solution = Solution()
    prices = [7,1,5,3,6,4]
    print(solution.maxProfit(prices))