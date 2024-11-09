
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        current = nums[0]
        times = 1
        counter = 1

        for _ in range(1, len(nums)):
            if(nums[counter] == current and times==1):
                counter += 1
                times += 1
            elif (nums[counter] == current and times == 2):
                nums.pop(counter)
            elif  (nums[counter] != current):
                current = nums[counter]
                times = 1
                counter +=1
        print(len(nums), nums)


if __name__ == "__main__":
    solution = Solution()
    nums = [0,0,1,1,1,1,2,3,3]
    print(solution.removeDuplicates(nums))