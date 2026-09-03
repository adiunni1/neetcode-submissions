class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char.lower() for char in s if char.isalnum())
        if clean == clean[::-1]:
            return True
        else:
            return False