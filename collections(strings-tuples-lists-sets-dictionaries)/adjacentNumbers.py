def find_adj_count(arr):
    count = 0
    for i in range(0, len(arr) - 1): # Fix is here
        if arr[i] == arr[i+1]: # Out of range exception - Index Error
            count += 1

    return count

#print(find_adj_count([1, 1, 5, 100, -20, -20, 6, 0, 0]))
# print(find_adj_count([10, 20, 30, 40, 30, 20]))
print(find_adj_count([1, 2, 2, 3, 4, 4, 4, 10]))