class Solution:
    def twoSum(self, nums: List[int], target: int) ->List[int]:
        seet={}
        for i,num in enumerate(nums):
            complements=target-num
            if complements in seet:
                return [seet[complements],i]
            seet[num]=i
        
