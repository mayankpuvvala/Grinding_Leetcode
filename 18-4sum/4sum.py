class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        a=0
        res= []
        nums.sort()
        while a<len(nums)-3:
            if a>0 and nums[a]==nums[a-1]:
                a+=1
                continue
            b= a+1
            while b<len(nums)-2:
                if b>a+1 and nums[b]==nums[b-1]:
                    b+=1
                    continue
                c= b+1
                d= len(nums)-1
                while c<d:
                    sumation = nums[a]+ nums[b] + nums[c] + nums[d]
                    if sumation > target :
                        d-=1
                    elif sumation < target:
                        c+=1
                    else:
                        res.append([nums[a], nums[b] , nums[c] , nums[d]])
                        while c<d and nums[c]== nums[c+1]:
                            c+=1
                        while c<d and nums[d] == nums[d-1]:
                            d-=1
                        c+=1
                        d-=1
                b+=1
            a+=1
        return res