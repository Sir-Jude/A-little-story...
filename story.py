# Level one
next_level = False
print("You wakes up in a dirty cell.")
print("You can move around (type \"move\")")
print("You can look around (type \"look\")")
print()

# The loop for the first level begins
while next_level == False:
    choice = input("What do you want to do? ").lower()
    print()
    if choice == "move":
        print("You cannot move around, because your wrists are handcuffed by a huge chain bonded to the wall.")    
    elif choice == "look":
        print("Next to you there is a skeleton.")
        next_level = True
    else:
        print("I did not get what you said: you can only choose between \"move\" and \"look\".")
print()

# Level two
next_level = False
print("The skeleton is pretty disgusting, but it may be useful...")
print("You can play with the skeleton (type \"play\")")
print("You can try to tear away the chain from the wall (type \"conan\")")
print()

# The loop for the second level begins
while next_level == False:
    choice = input("What do you want to do? ").lower()
    print()
    if choice == "play":
        print("A rat comes out from behind a bones and bit your hand: you lose 2VP.")
    elif choice == "conan":
        print("You have remembered! You are Conan, a strong warrior and you easily tear away the chain from the wall")
        next_level = True
    else:
        print("I did not get what you said: you can only choose between \"play\" and \"conan\".")