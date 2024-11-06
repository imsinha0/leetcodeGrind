

class Solution:

    # can be improved using start and end pointers
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for startIndex in range(len(s)):
            repeats = False
            currentChars = []
            currentIndex = startIndex
            while (not repeats) & (currentIndex < len(s)):
                if s[currentIndex] not in currentChars:
                    currentChars.append(s[currentIndex])
                    currentIndex += 1
                    if len(currentChars) > longest:
                        longest = len(currentChars)
                else:
                    repeats = True
        return longest





if __name__ == '__main__':
    solution = Solution()

    print(solution.lengthOfLongestSubstring("pwwkew"))