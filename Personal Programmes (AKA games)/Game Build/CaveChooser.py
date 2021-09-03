import random, time, BattleMechanic
def chooseCave():
    print('You are in a land full of dragons.')
    time.sleep(1)
    print('In front of you, you see two caves.')
    time.sleep(1)
    print('In one cave, the dragon is friendly and will share his treasure with you.')
    time.sleep(1)
    print('The dragon in the other cave is greedy and hungry, and will eat, but not before making you fight for his entertainment.')
    time.sleep(1)
    return int(input("Which cave will you go into? (1 or 2): "))

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(1)
    print('It is dark and spooky...')
    time.sleep(1)
    print('A large dragon appears in front of you and...')
    time.sleep(1)

    #friendlyCave = random.randint(1, 2)
    friendlyCave = 1

    if chosenCave == friendlyCave:
         print('Gives you his treasure!')
    else:
        print('Starts a fight, with his friend!!\n')
        time.sleep(1)
        BattleMechanic.main(random.randint(1,3))
        if BattleMechanic.battleWin == True:
            print("You won! The dragon is a creature of it's word, and you take their treasure")
        else:
            print("You lose, the dragon swallows you in one bite!")

def main():
    while True:
        try:
            caveNumber = chooseCave()
            checkCave(caveNumber)
            break
        except ValueError:
            print("\nWait a second, we're looking for a number! Try again...\n")