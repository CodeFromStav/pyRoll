import random
import time

#Create a training dummy with Health & Armor
#Have a dice roll determine the damage you do
#self is used to rep the instance of the class
class Dummy:
    def __init__(self, health, armor):
        self.health = health
        self.armor = armor
        
    def displayStats(self):
        print("Health:" + str(self.health))
        print("Armor:" + str(self.armor))

#random number generator chooses damage
class Hero:
    def __init__(self, health, armor):
        self.health = health
        self.armor = armor

    def meleeAttack(self, enemy):
        attack = 10
        melee = round(random.uniform(1,2), 1)
        attackTotal = (attack * melee)

        enemy.health -= attackTotal
        print("melee rolled: " + str(melee))
        print("final blow = " + str(attackTotal))


#===Character===
print("Type the name of the character you wish to choose: ")
print("{Elf, HP: 90, Def: 6}, {Dwarf, HP: 120, Def: 12}, {Human, HP: 100, Def: 10}")

char_select = input()
if char_select.lower() == "elf":
    mainChar = Hero(90,6)
    print("You have chosen Elf!")
    print("Your Stats: " + "Health: " + str(mainChar.health) + " Armor: " + str(mainChar.armor) + "\n")

elif char_select.lower() == "dwarf":
    mainChar = Hero(120,12)
    print("You have chosen Dwarf!")
    print("Your Stats: " + "Health: " + str(mainChar.health) + " Armor: " + str(mainChar.armor) + "\n")
    

elif char_select.lower() == "human":
    mainChar = Hero(100,10)
    print("You have chosen Human!")
    print("Your Stats: " + "Health: " + str(mainChar.health) + " Armor: " + str(mainChar.armor) + "\n")

else:
    print("Invalid Input. Rerun program. \n" )


#===Dummy===
print("Select Dummy Level: ")
print("{Easy, HP: 90, Def: 5}, {Intermediate, HP: 120, Def: 10}, {Advanced, HP: 200, Def: 15} ")

dummy_select = input()
if dummy_select.lower() == "easy":
    mainDummy = Dummy(90,5)
    print("You have chosen Easy!")
    print("Dummy Stats: " + "Health: " + str(mainDummy.health) + " Armor: " + str(mainDummy.armor) + "\n")

elif dummy_select.lower() == "intermediate":
    mainDummy = Dummy(120,10)
    print("You have chosen Intermediate!")
    print("Dummy Stats: " + "Health: " + str(mainDummy.health) + " Armor: " + str(mainDummy.armor) + "\n")

elif dummy_select.lower() == "advanced":
    mainDummy = Dummy(200,15)
    print("You have chosen Advanced!")
    print("Dummy Stats: " + "Health: " + str(mainDummy.health) + " Armor: " + str(mainDummy.armor) + "\n")

else:
    print("Invalid Input. Rerun program. \n")



print("The Fight Will Begin in: ")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

print("FIGHT!")




roundCount = 0
while mainDummy.health > 0:
    mainChar.meleeAttack(mainDummy)
    roundCount += 1
    print("Dummy Health: " + str(mainDummy.health) + "\n")
    time.sleep(1)

print("Victory in " + str(roundCount) + " rounds!")

# # # #test
# roundCount = 0

# while dummyOne.health > 0:
#     heroOne.meleeAttack(dummyOne)
#     roundCount += 1
#     print("Dummy Health: " + str(dummyOne.health) + "\n")

# print("Dummy Down!")
# print("Round Count: " + str(roundCount))

# overKill = dummyOne.health
# print("Overkill value: " + str(overKill))

# dummyOne.displayStats()


# # levelBeg = Dummy(50, 10)
# # levelInter = Dummy(100, 15)
# # levelAdv = Dummy(200, 20)
# # heroOne = Hero(150, 20)
# # heroOne.meleeAttack()
# # levelAdv.displayStats()


