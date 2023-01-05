
import random
def game(computer,you):
    if computer == you:
        return None
    elif computer == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    elif computer == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True     

    elif computer == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True            


print("computer turn: snake(s) water(w) or gun(g)?")
randno = random.randint(1,3)
print(randno)

if randno ==1:
    computer = 's'
elif randno == 2:
    computer = 'w' 
elif randno == 3:
    computer = 'g'   

you = input("your turn: snake(1) water(2) or gun(3)?")

a = game(computer, you)

print(f"computer choose {computer}")
print

if a == None:
    print("the game is a tie!")
elif a:
    print("you win!")    

else :
    print("you lose!")     