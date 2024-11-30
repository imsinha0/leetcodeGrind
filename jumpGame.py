class Solution:
    def canJump(self, nums: list[int]) -> bool:
        '''
        if(nums[0] == 0):
            if(len(nums) > 1):
                return False
            return True

        for ind1 in range(len(nums)-1):
            if (nums[ind1] == 0):
                for ind2 in range(ind1-1, -1, -1):
                    if(ind1-ind2 < nums[ind2]):
                        break
                    if(ind2 == 0):
                        return False
        return True
        '''


        #alternate solution

        currentPos = 0
        maxReach = 0

        while(currentPos < len(nums) and currentPos <= maxReach):
            maxReach = max(maxReach, currentPos + nums[currentPos])
            currentPos += 1
        if(currentPos == len(nums)):
            return True
        return False






if __name__ == "__main__":
    solution = Solution()
    nums = [2, 0, 0]
    print(solution.canJump(nums))