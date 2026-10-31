
# Time Complexity: (O(n)) — counting and scanning the dictionary.
# Space Complexity: (O(n)) — frequency dictionary
class Solution:
    def MajorityElement(self,nums):
        self.nums = nums

        s_ = {}

        for i in range(len(nums)):
            if nums[i] not in s_:
                s_[nums[i]] = 1

            else:
                s_[nums[i]] += 1

        res = nums[0]
        for num in s_:
            if s_[num] > s_[res]:
                res = num

        if s_[res] > (len(nums)//2):
            return res

O = Solution()
arr = list(map(int, input().split()))
print(f"Most Repeated Element: {O.MajorityElement(arr)}")