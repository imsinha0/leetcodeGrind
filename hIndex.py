import math

class Solution:
    def hIndex(self, citations: list[int]) -> int:

        max_h = math.floor(sum(citations)**0.5)

        current_count = 0

        for h in range(max_h, -1, -1):
            for y in range(len(citations)-1, -1, -1):
                if(citations[y] >= h):
                    current_count += 1
                    citations.pop(y)
            if(current_count>=h):
                return h

        return 0





if __name__ == "__main__":
    solution = Solution()
    citations = [3,0,6,1,5]
    print(solution.hIndex(citations))