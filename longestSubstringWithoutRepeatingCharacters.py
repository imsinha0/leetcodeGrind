

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for startIndex in range(len(s)):
            repeats = False
            currentChars = []
            currentIndex = startIndex
            while (not repeats):
                if s[currentIndex] not in currentChars:
                    currentChars.append(s[currentIndex])
                    currentIndex += 1
                    if len(currentChars) > longest:
                        longest = len(currentChars)
                    if(currentIndex == len(s)-1):
                        return longest
                else:
                    repeats = True
        return longest



if __name__ == '__main__':
    solution = Solution()

    print(solution.lengthOfLongestSubstring("pwwkew"))