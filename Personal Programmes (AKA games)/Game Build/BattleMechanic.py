import random, time, webbrowser
def Startup(enemyType):
    global health,enemyHealth,enemyHealthMax,potions,enemyPotions,potionStrength,playerchoice,gameMode,damageMIN,damageMAX,enemyName,enemyDamageMIN,enemyDamageMAX
    health,potions,potionStrength,playerchoice,gameMode,damageMIN,damageMAX = 10,3,5,24997,True,1,5
    if enemyType == 1:
        enemyName,enemyHealth,enemyHealthMax,enemyPotions,enemyDamageMIN,enemyDamageMAX = "goblin",10,10,3,1,5
    elif enemyType == 2:
        enemyName,enemyHealth,enemyHealthMax,enemyPotions,enemyDamageMIN,enemyDamageMAX = "kronenburg",1,1,0,0,1
    else:
        enemyName,enemyHealth,enemyHealthMax,enemyPotions,enemyDamageMIN,enemyDamageMAX = "giant troll",20,20,2,3,10
def Menu():
    print ("\nYou:",health,"HP and",potions,"Health potions")
    print ("Enemy:",enemyHealth,"HP and",enemyPotions,"Health potions\n")
    time.sleep(1)
    print ("1)  Attack ("+str(damageMIN)+"-"+str(damageMAX)+" damage)")
    print ("2)  Heal ("+str(potionStrength),"hp)")
    print ("3)  Run")
    print ("4)  Change weapon")
    print ("10) Developer's site")
    time.sleep(1)
    return int(input("\nSelect your choice: "))
def EnemyMove():
    global  health, enemyHealth, enemyPotions
    if enemyHealth >= (enemyHealthMax/2) or enemyPotions == 0: #Enemy will not try to heal if health is high, or it is out of potions
        enemyChoice = 1
    elif enemyHealth <= (enemyHealthMax/5) and enemyPotions > 0: #Enemy will automatically heal if health is under 20%, and it has a potion
        enemyChoice = 3
    else:
        enemyChoice = random.randint(1, 3)
    if enemyChoice <= 2:
        damage = random.randint(damageMIN,damageMAX)
        health = health - damage
        print("\nYou took",damage,"point(s) of damage. You have",health,"hp remaining")
        time.sleep(2)
    else:
        enemyHealth = enemyHealth + potionStrength
        print("\nThe",enemyName,"restored it's health. It has",enemyHealth,"hp remaining.\n")
        enemyPotions -= 1
        time.sleep(2)
        if enemyHealth > enemyHealthMax:
            print ("The",enemyName,"exceeded maximum heath, reducing back to 10 HP")
            enemyHealth = 10
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
    if weaponchoice == 1: #Sword
        damageMIN = 1
        damageMAX = 5
    elif weaponchoice == 2: #Knife
        damageMIN = 2
        damageMAX = 3
    elif weaponchoice == 3: #Gun
        damageMIN = 0
        damageMAX = 7
    elif weaponchoice == 5: #instakill
        damageMIN = 50
        damageMAX = 100
    else:
        print("Number not recognised, please try again")

def main(enemyTypeChoice):
    global health,enemyHealth,potions,enemyPotions,potionStrength,playerchoice,gameMode,damageMIN,damageMAX,enemyName,enemyDamageMIN,enemyDamageMAX, battleWin
    Startup(enemyTypeChoice)
    print("Welcome to the battle. you start with", health ,"hp!")
    while health>0 and enemyHealth>0:
        try:
            playerchoice = Menu()
        except ValueError:
            print("\nWait a second, we're looking for a number! Try again...")
            playerchoice = 24997
        #Battle Mechanics below!
        if playerchoice == 1: #Attack
            attack = random.randint(damageMIN,damageMAX)
            enemyHealth = enemyHealth - attack
            print("\nYou caused",attack,"point(s) of damage. The",enemyName,"has",enemyHealth,"hp remaining")
            time.sleep(2)
            if enemyHealth <= 0:
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
            health, enemyHealth = 0, 0
        elif playerchoice == 9001: #Exit
            health = 0
        elif playerchoice == 24997: #Default
            continue
        else:
            print("\nThe option you have chosen is not within the menu. Please try again.\n")
            time.sleep(2)
    if health>0:
        battleWin = True
    elif enemyHealth>0:
        battleWin=False
    else:
        print("It was a draw! That's awkward, this shouldn't actually be possible...")