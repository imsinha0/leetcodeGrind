class Solution:
    '''
    def removeDuplicates(self, nums: list[int]) -> int:
        seenElements = []
        counter = 0
        for _ in range(len(nums)):
            if(nums[counter] in seenElements):
                nums.pop(counter)
            else:
                seenElements.append(nums[counter])
                counter += 1
        return len(nums), nums
    '''

    def removeDuplicates(self, nums: list[int]) -> int:
        current = nums[0]
        counter = 1
        for _  in range(1, len(nums)):
            if(nums[counter] == current):
                nums.pop(counter)
            else:
                current = nums[counter]
                counter += 1
        return len(nums), nums


if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,1,1,1,1,1,1,1,2]
    print(solution.removeDuplicates(nums))













