number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# get the first, exclude the second
sliced_list = number_list[4:7]
print(sliced_list)

# 
sliced_list = number_list[:7]
print(sliced_list)

# 
sliced_list = number_list[:7:2]
print(sliced_list)

# 
sliced_list = number_list[::2]
print(sliced_list)

# 
sliced_list = number_list[::-1]
print(sliced_list)