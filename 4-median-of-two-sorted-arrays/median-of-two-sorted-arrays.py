class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newt=[]
        i,j=0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                newt.append(nums1[i])
                i+=1
            else:
                newt.append(nums2[j])
                j+=1
        while i<len(nums1):
            newt.append(nums1[i])
            i+=1
        while j<len(nums2):
            newt.append(nums2[j])
            j+=1
        mid= len(newt)//2
        if len(newt)%2!=0:
            return newt[mid]
        return (newt[mid]+newt[mid-1])/2