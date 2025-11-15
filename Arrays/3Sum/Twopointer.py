class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-1,0,1,2,-1,-4]
        nums.sort()
        #[-4,-1,-1,0,1,2]
        res=set()
        for i in range(0,len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target = nums[i]
            j=i+1
            k = len(nums)-1
            while j<k:
                    z= (nums[j]+nums[k])*-1
                    if z == target:
                         op=tuple([nums[i],nums[j],nums[k]])
                         res.add(op)
                         k=k-1
                         j=j+1
                         #print(f"equal j:{j} k:{k} z:{z} target:{target}")
                    elif z < target:
                        k=k-1
                        #print(f"geater j:{j} k:{k} z:{z} target:{target}")
                    else:
                        j=j+1 
                        #print(f"smaller j:{j} k:{k} z:{z} target:{target}")
        return [list(out) for out in res]
             
