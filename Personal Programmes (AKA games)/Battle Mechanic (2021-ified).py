"""
Created By: George Chachanidze
Game Version: Alpha 0.21
Last Edited: 09/07/21
"""
import random, time, webbrowser
health, enemyhealth, potions, enemypot, att, gamemode, DamageMIN, DamageMAX = 10, 10, 3, 3, 24997, True, 1, 5
def menu():
    print ("\nYou have:",health,"HP and",potions,"Health potions\n")
    time.sleep(1)
    print ("1) Attack (",DamageMIN,"-",DamageMAX,"damage)")
    print ("2) Heal (5 hp)")
    print ("3) Run")
    print ("4) Change weapon")
    print ("10) Developer's site")
    time.sleep(1)
    return int(input("\nSelect your choice: "))
def replay(choice):
        print("")
        if choice == ("yes") or choice == ("True") or  choice == ("1"):
            gamemode == True
        elif choice == ("no") or choice == ("False") or  choice == ("0"):
            exit()
        else:
            print("Input not understood, game will now shut down.")
            time.sleep(2)
            exit()
def EnemyMove():
    global enemypot, enemyhealth, health
    gobbchoice = random.randint(1, 3)
    if gobbchoice <= 2:
        damage = random.randint(1, 5)
        health = health - damage
        print("\nYou took",damage,"point(s) of damage. You have",health,"hp remaining\n")
        time.sleep(2)
    else:
        if enemypot > 0:
            enemyhealth = enemyhealth + 5
            print("\nThe goblin restored it's health. It has",enemyhealth,"hp remaining.\n")
            enemypot = enemypot - 1
            time.sleep(2)
            if enemyhealth > 10:
                print ("The Goblin exceeded maximum heath, reducing back to 10 HP")
                enemyhealth = 10
                time.sleep(2)
        else:
            print ("Goblin tried to heal but ran out of potions")
def WeaponPicker():
    global DamageMIN, DamageMAX
    print("\nWeapons Menu:")
    print("1) Sword (1-5 damage)")
    print("2) Knife (2-3 damage)")
    print("3) Gun (0-7 damage)")
    weaponchoice = int(input("\nPick a weapon: "))
    if weaponchoice == 1:
        DamageMIN = 1
        DamageMAX = 5
    elif weaponchoice == 2:
        DamageMIN = 2
        DamageMAX = 3
    elif weaponchoice == 3:
        DamageMIN = 0
        DamageMAX = 7
while gamemode == True:
    print("Welcome to the battle. you start with 10 hp!")
    while health>0 and enemyhealth>0:
        try:
            att = menu()
        except ValueError:
            print("\nWait a second, we're looking for a number! Try again...")
        #Battle Mechanics below!
        if att == 1: #Attack
            attack = random.randint(DamageMIN,DamageMAX)
            enemyhealth = enemyhealth - attack
            print("\nYou caused",attack,"point(s) of damage. The goblin has",enemyhealth,"hp remaining")
            time.sleep(2)
            if enemyhealth <= 0:
                break
            EnemyMove()
        elif att == 2: #Heal
            if potions > 0:
                health = health + 5
                print("\nHealth restored. You have", health, "hp remaining")
                potions = potions - 1
                time.sleep(2)
                if health > 10:
                    print ("\nYou have exceeded maximum heath, reducing back to 10 HP")
                    deduce = health - 10
                    health = health - deduce
                    time.sleep(2)
            else:
                print("\nYou tried to heal but you have run out of potions")
                time.sleep(2)
            EnemyMove()
        elif att == 3: #Run
            print ("\nCoward! Continue the fight!")
            time.sleep(2)
            EnemyMove()
        elif att == 4: #Change Weapon
            weapon = WeaponPicker()
        elif att == 10: #Website
            webbrowser.open('https://www.youtube.com/c/SnappyTech')
            exit()
        elif att == 69: #End Fight
            print("Suicide Fatality\n")
            time.sleep(1)
            health = 0
        elif att == 9001: #Exit
            exit()
        elif att == 24997: #Default
            print()
        else:
            print("\nThe option you have chosen is not within the menu. Please try again.\n")
            time.sleep(2)
    if health>0:
        print ("Well done, you won!")
        replay (input("Do you wish to replay? (yes or no): "))
    elif enemyhealth>0:
        print("Unlucky, you lost.")
        replay (input("Do you wish to replay? (yes or no): "))
    else:
        print("It was a draw!")
        replay (input("Do you wish to replay? (yes or no): "))