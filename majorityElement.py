
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = -1
        count = 0

        for element in nums:
            if(count == 0):
                candidate = element
                count = 1
            elif(candidate == element):
                count += 1
            else:
                count -=1

        return candidate




if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,3]
    print(solution.majorityElement(nums))