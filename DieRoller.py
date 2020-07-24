import random

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
        attackTotal = attack * melee

        enemy.health -= attackTotal
        print("melee rolled: " + str(melee))
        print("final blow = " + str(attackTotal))


dummyOne = Dummy(100, 10)
heroOne = Hero(100, 10)

# #test
roundCount = 0

while dummyOne.health > 0:
    heroOne.meleeAttack(dummyOne)
    roundCount += 1
    print("Dummy Health: " + str(dummyOne.health) + "\n")

print("Dummy Down!")
print("Round Count: " + str(roundCount))

overKill = dummyOne.health
print("Overkill value: " + str(overKill))

# dummyOne.displayStats()


# levelBeg = Dummy(50, 10)
# levelInter = Dummy(100, 15)
# levelAdv = Dummy(200, 20)
# heroOne = Hero(150, 20)
# heroOne.meleeAttack()
# levelAdv.displayStats()


