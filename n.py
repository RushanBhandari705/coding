arr = [5,4,1,2,6,8]

sorted_arr = sorted(arr, key=lambda x: (x % 2, x))
print(sorted_arr)  
# [2, 4, 8, 1, 3, 5]
