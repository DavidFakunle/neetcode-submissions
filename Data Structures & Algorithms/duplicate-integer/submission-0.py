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
        duplicate = []
        for num in nums:
            if num in duplicate:
                return True
            else:
                duplicate.append(num)

        return False