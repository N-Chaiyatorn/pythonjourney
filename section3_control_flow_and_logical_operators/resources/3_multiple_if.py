""" Multiple if """

iq = int(input("what is your iq?\n"))
isKid = input("are you a kid? Y or N\n")

if iq > 120:
    if isKid == "Y":
        print("You're genius kid")
    else:
        print("You're genius adult")
elif iq >= 100:
    print("You're smart")
else:
    print("You're normal")


isWantToIncreaseIq = bool(input("Want to increase iq? Type 'True' if true or press enter if false\n"))

""" Tips: Boolean variables don't need to compare with True or False, you can use it after if/elif directly """
if (isWantToIncreaseIq):
    iq += 20
    print(f"Your iq is increased by 20, now iq = {iq}")
else:
    print("Your iq is the same")
