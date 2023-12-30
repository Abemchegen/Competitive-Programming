class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]

        for i in range(max(len(nums1),len(nums2))):
            if len(nums1)>len(nums2):
                if nums1[i] in nums2:
                    ans.append(nums1[i])
                    nums2.remove(nums1[i])
            else:
                if nums2[i] in nums1:
                    ans.append(nums2[i])
                    nums1.remove(nums2[i])
        return ans
        