nums1 = [-5, -2, 4, 5, 0, 0, 0]
nums2 = [-3, 1, 8]

m = 4
n = 3

i = m - 1
j = n - 1 
k = m + n - 1

while j >= 0:
    if i >= 0 and nums1[i] < nums2[j]:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1

    elif i >= 0 and nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        k -= 1
        i -= 1

    else:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

print(nums1)