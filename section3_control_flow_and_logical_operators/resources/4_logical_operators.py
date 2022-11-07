""" Logical Operators """

iq = int(input("what is your iq?\n"))
isKid = bool(input("are you a kid? Type 'True' if true or press enter if false\n"))

if iq > 120 and isKid:
    print("You're genius kid")
elif iq > 120 and not isKid:
    print("You're genius adult")
elif iq >= 100:
    print("You're smart")
else:
    print("You're normal")
