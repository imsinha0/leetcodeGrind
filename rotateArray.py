
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k% n
        if (n != 1 and k != 0):
            nums[:] = (nums[-k:] + (nums[:n - k]))


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    print(solution.rotate(nums, k))