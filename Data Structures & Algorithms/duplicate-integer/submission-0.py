class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapper = set()
        for x in nums:
            if x not in mapper:
                mapper.add(x)
            else:
                return True
        return False