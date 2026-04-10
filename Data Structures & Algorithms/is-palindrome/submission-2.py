class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<right:
            ##if left is not alphanumeric, move left, same for right
            ##if left not equal to right, return false
            ##if left = right, increment both

            if s[left].isalnum() == False:
                left += 1
                continue
            if s[right].isalnum() == False:
                right = right - 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right = right-1
            
        return True