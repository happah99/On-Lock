import os
import random

divider = "=========================================================================================="
subDivider = "------------------------------------------------------------------------------------------"

inventory = []

health = 100
guardHealth = 100

def cell():
    os.system("cls")

    print("""
       ____          _                _    
      / __ \        | |              | |   
     | |  | |_ __   | |     ___   ___| | __
     | |  | | '_ \  | |    / _ \ / __| |/ /
     | |__| | | | | | |___| (_) | (__|   < 
      \____/|_| |_| |______\___/ \___|_|\_\ \n                                           
        © Created by SeigIndustries
        
        """)

    print(divider)
    print("You slowly open your eyes, head throbbing,")
    print("Looking around you find yourself in a cramped cell with rusting metal bars holding you captive,")
    print("You look down and realise you're wearing a stained orange jumpsuit!")
    print("The shouts and screams of the outside world PENETRATE you as you lay in a confused daze...")
    print(divider)

    answer = input("\n1. Scream and thrash 2. Gaze around :")

    if answer == "1":
        
        #instantDeath()
        hallway()

    elif answer == "2":
        os.system("cls")
        
        print(subDivider)
        print("As you gaze around the cell, you lock eyes on a key lying by the cell door,")        
        print("You muster the strength to get out of your cot and slowly approach the door.")
        print(subDivider)

        cellTwo()                 
    
    else:
        print("\nAre you illiterate?")      


def instantDeath():
    os.system("cls")
    
    print(subDivider)
    print("You suddenly hear heavy boots thundering toward you,")
    print("A hulking figure appears, picks you up by the neck as you slowly fade out of conciousness")
    print(subDivider)
    print("\n")

    input("YOU ARE DEAD. PRESS ANY KEY TO CONTINUE...")
    cell()


def cellTwo():
    
    answer = input("\n1. Kick the door 2. Open the door  3. Pick up the key :")
    if answer == "1":
        global health
        health -= 10

        print("\n"+subDivider)
        print("Your feeble malnorished frame can't handle the impact of the kick and you feel an immense pain.")
        print(subDivider)
        print("\nYOU LOSE 10 POINTS OF HEALTH...")
        print("Health:", health)
        
        if health == 0:
            os.system("cls")
            
            print(subDivider)
            print("You finally feel your bones shatter and your vision starts to fade.")
            print("Health:", health)
            print(subDivider, "\n")
            
            input("YOU ARE DEAD. PRESS ANY KEY TO CONTINUE...")

            cell()

        cellTwo()
    
    elif answer == "2":
        os.system("cls")

        if "KEY" in inventory:

            print(subDivider)
            print("As the key turns, the cell door slowly creaks on its rusting hinges.")
            print("You enter a dark hallway that's only lit by streams of light seeping through the cracks in the wall.")
            print(subDivider, "\n")

            inventory.remove("KEY")
            os.system("cls")
            hallway()
    
        else:
            print("\nThis door is locked")
            input("\nPRESS ANY KEY TO CONTINUE...")
            cellTwo()
    
    elif answer == "3":
        if "KEY" not in inventory:

            inventory.append("KEY")
            
            print("\n"+subDivider)
            print("You stumble over to the key, reach down and pick it up.\n")
            print("KEY ADDED TO INVENTORY")
            print(subDivider)

            print("\nInventory:", inventory)

            cellTwo()
        else:
            print("\n", subDivider)
            print("Are you blind?!")
            print("There is no key on the floor anymore...")
            print(subDivider, "\n")
            input("PRESS ANY KEY TO CONTINUE...")

            cellTwo()
    
    else:
        print("\nYou suddenly feel nauseous and pass out...")
        input("PRESS ANY KEY TO CONTINUE...")
        cell()   

darkSide = False

itemsToFind = ["RAZOR BLADE", "RUSTY NAIL", "DECEASED RAT"]

def hallway():
    global itemsToFind

    print("\n"+divider)
    print("The hallway is split into two directions, left and far right.")
    print("The left side is barely visible to your damaged eyes after your time in the darkness")
    print("However, on the far right side you can vaguely see light at the end...")
    print(divider, "\n")

    answer = input("1. Explore far right 2. Explore left :")
    
    if answer == "1":
        os.system("cls")

        print("\n"+subDivider)
        print("You edge around the corner and see the silhouette of a man that looks almost like a wild beast")
        print("The huge figure turns to face you as you are spotted")
        print("Your glutius maximus clenches in anticipation to the upcoming fight...")
        print(subDivider+"\n")
    
    elif answer == "2":
        os.system("cls")            

        left(darkSide)

    else:
        global health
        health -= 1

        print("\n"+subDivider)
        print("Get a grip you coward, there's no turning back now.")
        print(subDivider+"\n")
        print("YOU LOSE 1 POINTS OF HEALTH...")
        print("Health:", health, "\n")
    
        input("PRESS ANY KEY TO CONTINUE...")
        hallway()

def left(visited):
    global darkSide

    if visited == False:
        darkSide = True

        print("\n"+subDivider)
        print("As you turn left into the darkness you realize it's a dead end.")
        print("The darkness overwhelms you and ushers you away.")
        print(subDivider, "\n")
        input("1. Turn back :")

        hallway()
    
    else:
        print("\n"+subDivider)
        print("As you turn left again, your eyes grow accustomed to the dark")
        print("You can vaguely see the outline of unidentified objects littered on the floor.")
        print("There might be something useful in the dark...")
        print(subDivider, "\n")

        answer = input("1. Turn back 2. Rummage around in the dark :")

        if answer == "1":
            
            hallway()
        
        elif answer == "2":
            
            if len(itemsToFind) == 0:
                global health
                health -= 10

                print("\n"+subDivider)
                print("A live rat takes a chunk from your skeletal fingers")
                print("You almost let out a ghastly scream of pain...")
                print(subDivider)
                print("\nYOU LOSE 10 POINTS OF HEALTH...")
                print("Health:", health)

            else:
                os.system("cls")

                x = len(itemsToFind)-1
                item = itemsToFind[random.randint(0, x)]
                inventory.append(item)
                itemsToFind.remove(item)

                print("\n"+subDivider)
                print("You rummage around and pick up an item.\n")
                print(item+" ADDED TO INVENTORY")
                print(subDivider)
                    
                print("\nInventory:", inventory)
                print("\n")

                input("1. Turn back :")

                hallway()

cell()