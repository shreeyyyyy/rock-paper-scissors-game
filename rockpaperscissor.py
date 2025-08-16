import random
computer = random.choice([-1, 0, 1])
print("for rock enter r \nfor paper enter p \nfor scissor enter s")
youstr = input("ente your choice:")
yoydict={"r": 1, "p": -1, "s": 0}

if yoydict[youstr] == 1 and computer== 1:
    print("tie")
elif yoydict[youstr] == -1 and computer == -1:
    print("tie")
elif yoydict[youstr] == 0 and computer == 0:
    print("tie")
elif yoydict[youstr] == 1 and computer == 0:
    print("you win")
elif yoydict[youstr] == 0 and computer == -1:
    print("you win")
elif yoydict[youstr] == -1 and computer == 1:
    print("you win")
else:
    print("you lose")