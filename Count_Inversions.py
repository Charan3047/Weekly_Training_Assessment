class Solution:
    def merge(self, arr, left, mid, right):
        count = 0

        L = arr[left:mid+1]
        R = arr[mid+1:right+1]

        i = 0
        j = 0
        k = left

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                k += 1
                i += 1

            else:
                arr[k] = R[j]
                count += len(L) - i
                k += 1
                j += 1

        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1

        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1

        return count

    def merge_sort(self, arr, left, right):
        count = 0

        if left < right:
            mid = (left + right) // 2

            count += self.merge_sort(arr, left, mid)
            count += self.merge_sort(arr, mid + 1, right)
            count += self.merge(arr, left, mid, right)

        return count
    

O = Solution()
arr = list(map(int, input().split()))
print(f'No.of Inversions: {O.merge_sort(arr, 0 ,len(arr) - 1)}')