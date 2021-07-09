"""
Created By: George Chachanidze
Game Version: Alpha 0.1
Last Edited: 03/02/13
"""
import random, time, webbrowser

gamemode = True

def menu():
    print ("")
    print ("You have:",health,"HP and",potions,"Health potions")
    print ("")
    time.sleep(1)
    print ("1) Attack (1-5 damage)")
    print ("2) Heal (5 hp)")
    print ("3) Run")
    print ("5) Developer's site")
    time.sleep(1)
    print ("")
    return int(input("Select your choice: "))

def replay(choice):

        print("")
        if choice == ("yes"):
            gamemode == True
        elif choice == ("no"):
            exit()
        else:
            print("Input not understood, game will now shut down.")
            time.sleep(2)
            exit()

while gamemode == True:
    health = 10
    enemyhealth = 10
    potions = 3
    enemypot= 3
    print("Welcome to the battle. you start with 10 hp!")
    while health>0 and enemyhealth>0:
        gobbchoice = random.randint(1, 3)
        att = menu()
        #Battle Mechanics below!
        if att == 1: #If you attack
            attack = random.randint(1, 5)
            enemyhealth = enemyhealth - attack
            print("")
            print("You caused",attack,"point(s) of damage. The goblin has",enemyhealth,"hp remaining")
            time.sleep(2)
            if gobbchoice <= 2:
                damage = random.randint(1, 5)
                health = health - damage
                print("")
                print("You took",damage,"point(s) of damage. You have",health,"hp remaining")
                print("")
                time.sleep(2)
            else:
                if enemypot > 0:
                    enemyhealth = enemyhealth + 5
                    print("")
                    print("The goblin restored it's health. It has",enemyhealth,"hp remaining.")
                    print("")
                    enemypot = enemypot - 1
                    time.sleep(2)
                    if enemyhealth > 10:
                        print("")
                        print ("The Goblin exceeded maximum heath, reducing back to 10 HP")
                        deduce = health - 10
                        health = enemyhealth - deduce
                        time.sleep(2)

                else:
                    print ("Goblin tried to heal but ran out of potions")


        elif att == 2: #if you heal
            if potions > 0:
                health = health + 5
                print("")
                print("Health restored. You have", health, "hp remaining")
                potions = potions - 1
                time.sleep(2)
                if health > 10:
                    print("")
                    print ("You have exceeded maximum heath, reducing back to 10 HP")
                    deduce = health - 10
                    health = health - deduce
                    time.sleep(2)

            elif potions <= 0:
                print("")
                print("You tried to heal but you have run out of potions")
                time.sleep(2)

            if gobbchoice <= 2:
                damage = random.randint(1, 5)
                health = health - damage
                print("")
                print("You took",damage,"point(s) of damage. You have",health,"hp remaining")
                time.sleep(2)
            else:
                if enemypot > 0:
                    enemyhealth = enemyhealth + 5
                    print("")
                    print("The goblin restored it's health. It has",enemyhealth,"hp remaining.")
                    print("")
                    enemypot = enemypot - 1
                    time.sleep(2)
                    if enemyhealth > 10:
                        print("")
                        print ("The Goblin exceeded maximum heath, reducing back to 10 HP")
                        deduce = health - 10
                        health = enemyhealth - deduce
                        time.sleep(2)
                else:
                    print ("Goblin tried to heal but ran out of potions")

        elif att == 3:
            print("")
            print ("Coward! Continue the fight!")
            time.sleep(2)
            if gobbchoice <= 2:
                damage = random.randint(1, 5)
                health = health - damage
                print("")
                print("You took",damage,"point(s) of damage. You have",health,"hp remaining")
                print("")
                time.sleep(2)
            else:
                if enemypot > 0:
                    enemyhealth = enemyhealth + 5
                    print("")
                    print("The goblin restored it's health. It has",enemyhealth,"hp remaining.")
                    print("")
                    enemypot = enemypot - 1
                    time.sleep(2)
                else:
                    print ("Goblin tried to heal but ran out of potions")

        elif att == 5:
            webbrowser.open('snappy-tech.blogspot.com')
            exit()

        elif att == 69:
            time.sleep(1)
            print("Suicide Fatality")
            print("")
            time.sleep(1)
            health = 0

        elif att == 9001:
            exit()

        else:
            print("")
            print("The option you have chosen is not within the menu. Please try again.")
            print("")
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