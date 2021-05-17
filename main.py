import random

class Warrior():

    def __init__(self,n):
        self.life_points = random.randint(1,100)
        self.dmg_points = random.randint(1,20)
        self.initiative = random.randint(1,10)
        self.get_stats()
        self.name = n
        self.spells = ["fireball","thunder"]

    def defece(self,dmg):
        self.life_points -= dmg

        if self.life_points <= 0:
            self.life_points = 0

    def get_name(self):
        return self.name

    def check_if_alive(self):
        if self.life_points == 0:
            return False
        else:
            return True

    def get_life(self):
        return self.life_points

    def get_dmg(self):
        return self.dmg_points

    def get_initiative(self):
        return self.initiative

    def get_stats(self):
        print(self.life_points,self.dmg_points)

    def get_spell(self):
        return self.spells

class Wizard():

    def __init__(self,n):
        self.life_points = random.randint(1,100)
        self.dmg_points = random.randint(1,20)
        self.initiative = random.randint(1,10)
        self.get_stats()
        self.name = n
        self.spells = ["fireball","thunder"]

    def defece(self,dmg):
        self.life_points -= dmg

        if self.life_points <= 0:
            self.life_points = 0

    def get_name(self):
        return self.name

    def check_if_alive(self):
        if self.life_points == 0:
            return False
        else:
            return True

    def get_life(self):
        return self.life_points

    def get_dmg(self):
        return self.dmg_points

    def get_initiative(self):
        return self.initiative

    def get_stats(self):
        print(self.life_points,self.dmg_points)

    def get_spell(self):
        return self.spells

def walka(player1,player2):
    while player1.get_life() > 0 and player2.get_life() > 0:
        print(f"Player 1 has {player1.get_initiative()} initiative, Player 2 has {player2.get_initiative()} initiative")
        if player1.get_initiative() >= player2.get_initiative():
            player2.defece(player1.get_dmg())
            print("Player 1 attacks with",random.choice(player1.get_spell()))
            print(f"PLayer 2 got {player1.get_dmg()} damage! Now he's got {player2.get_life()} life left")
            if not player2.check_if_alive():
                print(player2.get_name()," died")
                return True
            player1.defece(player2.get_dmg())
            print("Player 2 attacks with",random.choice(player2.get_spell()))
            print(f"PLayer 1 got {player2.get_dmg()} damage! Now he's got {player1.get_life()} life left")
            if not player1.check_if_alive():
                print(player2.get_name()," died")
                return False
        else:
            player1.defece(player2.get_dmg())
            print("Player 2 attacks with",random.choice(player2.get_spell()))
            print(f"PLayer 1 got {player2.get_dmg()} damage! Now he's got {player1.get_life()} life left")
            if not player1.check_if_alive():
                print("Player 1 died")
                return False
            player2.defece(player1.get_dmg())
            print("Player 1 attacks with",random.choice(player1.get_spell()))
            print(f"PLayer 2 got {player1.get_dmg()} damage! Now he's got {player2.get_life()} life left")
            if not player2.check_if_alive():
                print("Player 2 died")
                return True

player1 = Warrior("Player1")
player2 = Warrior("Player2")

walka(player1,player2)

