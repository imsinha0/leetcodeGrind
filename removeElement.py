class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        i = 0 #index of nums
        count = 0
        #we want to loop through and send the val elements to the other side
        for _ in range(len(nums)):
            if(nums[i] == val):
                nums.append(nums.pop(i))
            else:
                i += 1
            count += 1
        return i, nums


if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,2,3]
    val = 3
    print(solution.removeElement(nums, val))


