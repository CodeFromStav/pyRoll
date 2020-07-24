import random

#main function


#random.randrange(start,stop[,step])
#random.randrange(stop)





#Create a training dummy with Health & Armor
#Have a dice roll determine the damage you do
#self is used to rep the instance of the class
class Dummy:
    def __init__(self, health, armor):
        self.health = health
        self.armor = armor

    # def meleeAttack():


    #def magicAttack():
        
    def displayStats(self):
        print("Health:" + str(self.health))
        print("Armor:" + str(self.armor))

#random number generator chooses damage
class Hero:
    def __init__(self, health, armor):
        self.health = health
        self.armor = armor

    def meleeAttack(self):
        attack = 10
        melee = random.randint(1,2)
        attack = attack * melee
        print("melee rolled: "+ str(melee))
        print("final blow = " + str(attack))


levelBeg = Dummy(50, 10)
levelInter = Dummy(100, 15)
levelAdv = Dummy(200, 20)

heroOne = Hero(150, 20)

heroOne.meleeAttack()

levelAdv.displayStats()


