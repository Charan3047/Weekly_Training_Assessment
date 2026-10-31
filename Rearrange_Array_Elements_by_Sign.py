class Solution:
  def Rearrange(self, nums):

    pos_index = 0
    neg_index = 1

    res = [0]*len(nums)

    for num in nums:
       if num > 0:
        res[pos_index] = num
        pos_index += 2
       else:
        res[neg_index] = num
        neg_index += 2

    return res

O = Solution()
arr = list(map(int, input().split()))
print(f"Rearranged Version:{O.Rearrange(arr)}")