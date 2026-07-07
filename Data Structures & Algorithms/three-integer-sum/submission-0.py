class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Understand- Return all triplets where the sum of i, j , k equals 0, and all are distinct
            input - nums array
            output - triplets array
            contraints- no duplicate triplets
            
        Plan-

        Implement- 
        '''

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # same Value
                continue# we dont want to use the same value

            l , r = i + 1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l< r:
                        l += 1

        return res