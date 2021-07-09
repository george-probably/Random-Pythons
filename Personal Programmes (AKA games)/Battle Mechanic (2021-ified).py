import random, time, webbrowser
def Startup():
    global health, enemyhealth, potions, enemypotions, playerchoice, gamemode, damageMIN, damageMAX
    health,enemyhealth,potions,enemypotions,playerchoice,gamemode,damageMIN,damageMAX = 10,10,3,3,24997,True,1,5
def Menu():
    print ("\nYou:",health,"HP and",potions,"Health potions")
    print ("Enemy:",enemyhealth,"HP and",enemypotions,"Health potions\n")
    time.sleep(1)
    print ("1) Attack (",damageMIN,"-",damageMAX,"damage)")
    print ("2) Heal (5 hp)")
    print ("3) Run")
    print ("4) Change weapon")
    print ("10) Developer's site")
    time.sleep(1)
    return int(input("\nSelect your choice: "))
def EnemyMove():
    global enemypotions, enemyhealth, health
    if enemyhealth >= 8 or enemypotions == 0:
        gobbchoice = 1
    elif enemyhealth <= 2:
        gobbchoice = 3
    else:
        gobbchoice = random.randint(1, 3)
    if gobbchoice <= 2:
        damage = random.randint(1, 5)
        health = health - damage
        print("\nYou took",damage,"point(s) of damage. You have",health,"hp remaining")
        time.sleep(2)
    else:
        enemyhealth = enemyhealth + 5
        print("\nThe goblin restored it's health. It has",enemyhealth,"hp remaining.\n")
        enemypotions = enemypotions - 1
        time.sleep(2)
        if enemyhealth > 10:
            print ("The Goblin exceeded maximum heath, reducing back to 10 HP")
            enemyhealth = 10
            time.sleep(2)
def WeaponPicker():
    global damageMIN, damageMAX
    picked = False
    print("\nWeapons Menu:")
    print("1) Sword (1-5 damage)")
    print("2) Knife (2-3 damage)")
    print("3) Gun (0-7 damage)")
    while picked==False:
        try:
            weaponchoice = int(input("\nPick a weapon: "))
            picked = True
        except ValueError:
            print("\nWait a second, we're looking for a number! Try again...")
    if weaponchoice == 1:
        damageMIN = 1
        damageMAX = 5
    elif weaponchoice == 2:
        damageMIN = 2
        damageMAX = 3
    elif weaponchoice == 3:
        damageMIN = 0
        damageMAX = 7
    else:
        print("Number not recognised, please try again")
def Replay(choice):
        print("")
        if choice == ("yes") or choice == ("True") or  choice == ("1"):
            gamemode == True
            Startup()
        elif choice == ("no") or choice == ("False") or  choice == ("0"):
            exit()
        else:
            print("Input not understood, game will now shut down.")
            time.sleep(2)
            exit()

Startup()
while gamemode == True:
    print("Welcome to the battle. you start with 10 hp!")
    while health>0 and enemyhealth>0:
        try:
            playerchoice = Menu()
        except ValueError:
            print("\nWait a second, we're looking for a number! Try again...")
            playerchoice = 24997
        #Battle Mechanics below!
        if playerchoice == 1: #Attack
            attack = random.randint(damageMIN,damageMAX)
            enemyhealth = enemyhealth - attack
            print("\nYou caused",attack,"point(s) of damage. The goblin has",enemyhealth,"hp remaining")
            time.sleep(2)
            if enemyhealth <= 0:
                break
            EnemyMove()
        elif playerchoice == 2: #Heal
            if potions > 0:
                health = health + 5
                print("\nHealth restored. You have", health, "hp remaining")
                potions = potions - 1
                time.sleep(2)
                if health > 10:
                    print ("\nYou have exceeded maximum heath, reducing back to 10 HP")
                    health = 10
                    time.sleep(2)
            else:
                print("\nYou tried to heal but you have run out of potions")
                time.sleep(2)
            EnemyMove()
        elif playerchoice == 3: #Run
            print ("\nCoward! Continue the fight!")
            time.sleep(2)
            EnemyMove()
        elif playerchoice == 4: #Change Weapon
            weapon = WeaponPicker()
        elif playerchoice == 10: #Website
            webbrowser.open('https://www.youtube.com/c/SnappyTech')
            exit()
        elif playerchoice == 69: #End Fight
            print("Suicide Fatality\n")
            time.sleep(1)
            health, enemyhealth = 0, 0
        elif playerchoice == 9001: #Exit
            exit()
        elif playerchoice == 24997: #Default
            print()
        else:
            print("\nThe option you have chosen is not within the menu. Please try again.\n")
            time.sleep(2)
    if health>0:
        print ("Well done, you won!")
    elif enemyhealth>0:
        print("Unlucky, you lost.")
    else:
        print("It was a draw! That's awkward, this shouldn't actually be possible...")
    Replay (input("Do you wish to replay? (yes or no): "))