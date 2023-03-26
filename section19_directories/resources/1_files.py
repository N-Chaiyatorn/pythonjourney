file = open("hi.txt")
contents = file.read()
print(contents)
file.close()

# read file using "with"
# with open("hi.txt") as file:
#     contents = file.read()
#     print(contents)

# overwrite file
# with open("hi.txt", mode="w") as file:
#     file.write("New text")

# append file
# with open("hi.txt", mode="a") as file:
#     file.write("New text")