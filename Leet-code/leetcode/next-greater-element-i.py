class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        d = {}

        for i in range(len(nums2) ):

            d[nums2[i]] = i

        st = []

        ans = [-1] * len(nums2)

        for i in range(len(nums2)) :

            while st and nums2[i] > nums2[st[-1]] :

                ans[st[-1]] = nums2[i]
                st.pop()

            st.append(i)
        out = []

        for i in range(len(nums1)) :

            out.append(ans[d[nums1[i]]])

        return out






        