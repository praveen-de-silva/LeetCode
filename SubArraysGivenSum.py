# =========================
# Find sub arrays given sum 
# -------------------------
# To solve this 'Sliding window' technique is used.
# Time Complexity : O(n)
# =========================

arr = [4, 1, 4, 2,2,3,1]

k = 4

n = len(arr)
l = 0
crntSum = 0
count = 0

for r in range(n):
    crntSum += arr[r]

    while crntSum > k and l <= r:
        crntSum -= arr[l]
        l+=1
        
    if crntSum == k:
        count += 1
        
print(count) 
