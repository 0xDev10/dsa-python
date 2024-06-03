def valid_palindrome(s: str) -> bool:
    i = 0
    j = len(s)-1    
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

s = ''
print(valid_palindrome(s))



# def validPalindrome2(s: str) -> bool:
#     isPalindrome = lambda s: s == s[::-1]
    
#     left, right = 0, len(s) - 1
#     half = len(s)//2
#     while left < right:
#         if s[left:left+half] == s[right:right-half:-1]:
#             left += half
#             right -= half
#         elif half > 1:
#             half = half//2
#         else:
#             return (
#                 isPalindrome(s[left:right]) or 
#                 isPalindrome(s[left+1:right+1]))
#     return True

# def check_palindrome(s: str) -> bool:
#     if s == s[::-1]:
#         return True
#     return False

# s = 'lev el'
# print(check_palindrome(s))