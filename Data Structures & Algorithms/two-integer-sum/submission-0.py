class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Understand- Given two integers in a list, return the indices i and j that add up to target
            input - nums, target 
            output - the two indices that add up to target
        Plan-
            create dict for the seen values 
            loop through nums
                define needed as target - nums[i]
                if needed in seen:
                    return[the seen value  and i ]

                
                if not add to dictionary
        Implement-

        '''

        seen = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in seen:
                return [seen[need], i]

        
            seen[nums[i]] = i