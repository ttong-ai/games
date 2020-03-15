from random import randint

my_score = 0
your_score = 0

for i in range(0, 6):
    t = input("Give me your hand [R]ock, [P]aper, [S]cissors: ")
    t = t.lower().strip()
    if t == 'r':
        t = "rock"
    elif t == 'p':
        t = 'paper'
    elif t == 's':
        t = 'scissors'
    if t not in ["rock", "scissors", "paper"]:
        print(f"Input '{t}' is not allowed.\n")
        continue

    guess = randint(1, 3)

    if guess == 1:
        # 1 Rock
        print("I have Rock!")
        if t == "rock":
            print("We are draw...")
        elif t == "scissors":
            print("I won this one...")
            my_score = my_score + 1
        elif t == "paper":
            print("oops, I lost this one...")
            your_score = your_score + 1

    elif guess == 2:
        # 2 Scissors
        print("I have Scissors!")
        if t == "scissors":
            print("We are draw...")
        elif t == "paper":
            print("I won this one...")
            my_score = my_score + 1
        elif t == "rock":
            print("oops, I lost this one...")
            your_score = your_score + 1

    else:
        # 3 paper
        print("I have Paper!")
        if t == "paper":
            print("We are draw...")
        elif t == "rock":
            print("I won this one...")
            my_score = my_score + 1
        elif t == "scissors":
            print("oops, I lost this one...")
            your_score = your_score + 1

    print("Here are our current scores")
    print("Computer (me):\t", my_score)
    print("Yours:\t\t", your_score)
    print()

print("Here are our final scores")
print("Computer (me):\t", my_score)
print("Yours:\t\t", your_score)
if my_score > your_score:
    print("Dude! I won!")
elif my_score < your_score:
    print("Dude! I lost to you!")
else:
    print("Oh!We are even!")
print("Bye-bye")
