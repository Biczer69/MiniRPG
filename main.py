import random

class Warrior():

    def __init__(self,n):
        self.life_points = random.randint(1,100)
        self.dmg_points = random.randint(1,20)
        self.initiative = random.randint(1,10)
        self.name = n
        self.attacks = ["fireball","thunder","meele"]
        self.get_stats()

    def defance(self,dmg):
        self.life_points -= dmg

        if self.life_points <= 0:
            self.life_points = 0

    def check_if_alive(self): #True if alive
        if self.life_points == 0:
            return False
        else:
            return True

    ####Functions that returne stats######

    def get_name(self):
        return self.name

    def get_life(self):
        return self.life_points

    def get_dmg(self):
        return self.dmg_points

    def get_initiative(self):
        return self.initiative

    def get_attacks(self):
        return self.attacks

    def get_stats(self):
        print(f"Name is: {self.name} life = {self.life_points},dmg = {self.dmg_points}, initiative = {self.initiative}")

    ########################################

def skirmish(player1,player2):
    print(player1.get_name(), "has higher initiative, therefore is first to attack!")
    while player1.check_if_alive and player2.check_if_alive:

            ###Attack
            player2.defance(player1.get_dmg())
            print(player1.get_name(), "attacks with" , random.choice(player1.get_attacks()))
            print(player2.get_name(), f"got {player1.get_dmg()} damage! Now he's got {player2.get_life()} life left")
            if not player2.check_if_alive():
                print(player2.get_name()," died!")
                return True

            ###Counterattack
            player1.defance(player2.get_dmg())
            print(player2.get_name(),"attacks with",random.choice(player2.get_attacks()))
            print(player1.get_name(),f"got {player2.get_dmg()} damage! Now he's got {player1.get_life()} life left")
            if not player1.check_if_alive():
                print(player1.get_name()," died")
                return False

player1 = Warrior(input("Podaj imię pierwszego wojownika!\n"))
player2 = Warrior(input("Podaj imię drugiego wojownika!\n"))

if player1.get_initiative() >= player2.get_initiative():
    skirmish(player1,player2)
else:
    skirmish(player2, player1)

