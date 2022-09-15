import random

def gameWin(comp, you):
    if comp == you:
        return None

    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True


print("Computer's turn: Rock(r) | Paper(p) | Scissors(s) ?--> ")
rand_num = random.randint(1, 3)

if rand_num == 1:
    comp = 'r'
elif rand_num ==2:
    comp = 'p'
elif rand_num == 3:
    comp = 's'

you = input("your turn: Rock(r) | Paper(p) | Scissors(s)?--> " )

result = gameWin(comp, you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if result == None:
    print("The game is a tie !!!")
elif result:
    print("You win ")
else:
    print("you lose")