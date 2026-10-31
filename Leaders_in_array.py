# Time Complexity: (O(n))
# Space Complexity: (O(n)) 

class Solution:
    def LeadersArray(self,nums):
        self.nums = nums

        leaders = []
        max_ = float('-inf')

        for num in nums[::-1]:
            if num > max_:
                leaders.append(num)
                max_ = num

        return leaders[::-1]

O = Solution()
arr = list(map(int, input().split()))
print(O.LeadersArray(arr))