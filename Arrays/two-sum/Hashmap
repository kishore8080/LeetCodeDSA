class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        res=[0,0]
        for i in range(0,len(nums)):
            x = target-nums[i]
            if x not in map:
                map[nums[i]]=i
            else:
                res[0]=i
                res[1]=map[x]
                return res
