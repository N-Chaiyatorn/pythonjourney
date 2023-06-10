#FileNotFound
with open("x.txt") as x:
    x.read()

#KeyError
dictionary = {"key":"value"}
value = dictionary("test")

#IndexError
list_a = [1,2,3]
list[3]

#TypeError
text = "test"
print(text + 5)


# Syntax for error(exception) catching
"""
try     = Code that might cause an exception
except  = Do this part if there is any exception
else    = Do this part if there is no exception
finally = Do this regardless
"""
try:
    file = open("a_file.txt")
    dictionary = {"key":"value"}
    print(dictionary["test"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("")
except KeyError as err:
    print("Key error", err)
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("closed file")


# custom exception
height = float(input("height: "))

if height >= 3:
    raise ValueError("Invalid height input")


# Quiz - Modify below code to sum the likes of each dict in the list without error, ignore dict without 'Likes' key
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    total_likes = total_likes + post['Likes']

print(total_likes)