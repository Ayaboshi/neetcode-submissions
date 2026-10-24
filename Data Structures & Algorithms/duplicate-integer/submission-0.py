class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        qc=set(nums)
        if len(qc)<len(nums):
            return True
        else :
            return False


