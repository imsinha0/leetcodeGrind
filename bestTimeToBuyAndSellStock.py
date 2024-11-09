


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''
        leftPointer = 0
        rightPointer = 1

        maxProfit = 0

        while(leftPointer <= len(prices)-2):
            while(prices[rightPointer] > prices[leftPointer]):
                maxProfit = max(maxProfit, prices[rightPointer] - prices[leftPointer])
                if(rightPointer == len(prices)-1):
                    return maxProfit
                rightPointer += 1
            leftPointer = rightPointer
            rightPointer = leftPointer+1

        return maxProfit
    '''

        current_max = 0
        maxPrice = 0
        for element in reversed(prices):
            maxPrice = max(maxPrice, (current_max - element))
            current_max = max(current_max, element)
        return maxPrice




if __name__ == "__main__":
    solution = Solution()
    prices = [2,6,3,1,1,1]
    print(solution.maxProfit(prices))