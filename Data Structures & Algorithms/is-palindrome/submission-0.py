class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ''.join(char.lower() for char in s if char.isalnum())
        return temp == temp[::-1]