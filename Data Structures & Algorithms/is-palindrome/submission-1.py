class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Understand- Return True if s is a palindrome, and return false if otherwise
            input - String s
            output - Boolean Value ; True or False
        Plan-
        set left pointer to 0
        set right pointer to the end of s
        if a character is not alphanumeric, move the pointer
        if it is alphanumeric, check compare the lowercased version
            if it fails return False
        if we never return False, return True at the end of loop 
        Implement-
        '''
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False

        return True #Space : O(1) , Time: O(n)