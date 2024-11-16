class Solution:
    def jump(self, nums: list[int]) -> int:

        max_reached = 0
        num_steps = 0
        max_in_step = 0


        for current_pos in range(len(nums)):
            if(max_in_step >= len(nums) - 1):
                return num_steps
            if(max_reached < current_pos+nums[current_pos]):
                max_reached = current_pos + nums[current_pos]
            if(max_in_step <= current_pos):
                max_in_step = max_reached
                num_steps += 1
        return num_steps




if __name__ == "__main__":
    solution = Solution()
    nums = [2,3,1,1,4]
    print(solution.jump(nums))