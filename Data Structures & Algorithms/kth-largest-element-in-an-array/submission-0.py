class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        while(k):
            max_num = max(nums)
            nums.remove(max_num)
            k-=1
        return max_num
