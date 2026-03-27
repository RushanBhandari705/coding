arr = [5, 2, 8, 3, 1, 4]

sorted_arr = sorted(arr, key=lambda x: (x % 2, x))
print(sorted_arr)  
# [2, 4, 8, 1, 3, 5]