def find_pairs(arr, target_sum):
    n = len(arr)
    pairs = []
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs


arr = [2, 4, 5, 1, 3, 6, 8]
target_sum = 9
print(find_pairs(arr, target_sum)) 