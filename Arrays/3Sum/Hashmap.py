 def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4,-1,-1,0,1,2]
        res=set()
        nums.sort()
        for i in range (0,len(nums)-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            z=nums[i]
            dic={}
            dic1={}
            print(f"i:{i}")
            for cur in range(i+1,len(nums)):
                y = -1*z-nums[cur]
                if y not in dic:
                    dic[nums[cur]]=cur
                    dic1[cur]=nums[cur]
                else:
                    op=[z,dic1[dic[y]],nums[cur]]
                    res.add(tuple(op))
                     
        return [list(op) for op in res]
