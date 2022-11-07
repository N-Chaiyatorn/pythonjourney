""" Nested if / else and elif """

iq = int(input("what is your iq?\n"))
isKid = bool(input("are you a kid? Type 'True' if true or press enter if false\n"))

if iq > 120:
    if isKid == True:
        print("You're genius kid")
    else:
        print("You're genius adult")
elif iq >= 100:
    print("You're smart")
else:
    print("You're normal")
