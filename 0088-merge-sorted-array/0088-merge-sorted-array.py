class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        counter = 0

        for x in range(len(nums1)):
            if x >= m:
                nums1[x] = nums2[counter]
                counter += 1

        nums1.sort()
            