class Solution:
    def validPalindrome(self, s: str) -> bool:
        isPalindrome = lambda s: s == s[::-1]
        
        left, right = 0, len(s) - 1
        half = len(s)//2
        while left < right:
            if s[left:left+half] == s[right:right-half:-1]:
                left += half
                right -= half
            elif half > 1:
                half = half//2
            else:
                return (
                    isPalindrome(s[left:right]) or 
                    isPalindrome(s[left+1:right+1]))
        return True