class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Understand- Given the String s, find the length of the longest substring without any duplicates
            input - string s
            output - integer : length of longest substring without repeating characters
            constraints - O(n) time and O(m) space
        Plan-
        Have a left pointer 
        intialize an empty hash set
        and use a right pointer looping through the len(s)
        and every loop using a hashset check  if all the values inside of left and right pointer ie does the window have duplicates
        while is s[right] is a duplicate move s[left] until there are no more duplicates 
        if its not add s[right] into the hash set 
        then calculae max_length using window lenght formula too ( right - left + 1)
        at the end return max_length
        Implement-
        '''
        l = 0
        no_duplicates = set()
        max_length = 0

        for r in range(len(s)):
            while s[r] in no_duplicates:
                no_duplicates.remove(s[l])
                l += 1
            
            no_duplicates.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length

