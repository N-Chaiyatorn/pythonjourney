# list variable vs original variable

# a = [1, 2, 3]
# b=a
# b[1] = 9
# print(a)    # ====> [1, 9, 3]


# c = 3
# d = c
# d=9
# print(f"{c}")           # ===> 3

a=3
b=a
a=5
print(b)