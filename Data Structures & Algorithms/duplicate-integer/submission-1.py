class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Understand- Given an integer array of nums, return true if any value occurs more than once
            input- nums array
            output- boolean True/False
        Plan-
            list = []
            loop through nums list
            if number in list already:
                return True
            else:
                append number to list

            return False at the end of loop
        Implement
        '''
        seen = set()
        for num in nums:
            if num in seen:
                return True

            seen.add(num)
        
        return False #Time: O(n) Space: O(n)