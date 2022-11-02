""" Type Conversion """

# Type Error
len(100)
"Hello" + 10

# Type Check
print(type(100))
print(type(15.123))
print(type("Hello"))
print(type(True))

# Type Conversion
print(type(str(100))) # First 100 is int, then converted to String
print(type(str("1.2345")))
print(type(int("1.0")))
print(type(float("1.0")))
# print(type(int("1.123")))
# print(type(int("asdqw")))
print(type(float(1)))