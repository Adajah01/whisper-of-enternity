# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:39:05 2023

@author: adaja
"""


from random import random, randint

# D100 dice roll
def diceroller():
    return 100 * (round(random(), 2))

class Player:
    def __init__(self, health, name, player_class):
        self.health = health
        self.name = name
        self.player_class = player_class

    def wound(self, damage):
        if self.health > 0:
            self.health -= damage
            print(f"{self.name} was struck for {damage}!!! Nice scar.")
            if self.health < 0:
                self.health = 0
        else:
            print("Your deeds will be remembered. Not really.")

class Strong(Player):
    def __init__(self, health, name, fighty):
        super().__init__(health, name, "Strong")
        self.fighty = 1

class Smart(Player):
    def __init__(self, health, name, clever):
        super().__init__(health, name, "Smart")
        self.clever = 1

class Fast(Player):
    def __init__(self, health, name, quick):
        super().__init__(health, name, "Fast")
        self.quick = 1

def select_player_class():
    print("Choose your player class:")
    print("1. Strong")
    print("2. Smart")
    print("3. Fast")

    choice = input("Enter the number corresponding to your choice: ")

    if choice == "1":
        return Strong(500, name, "fighty")
    elif choice == "2":
        return Smart(500, name, "clever")
    elif choice == "3":
        return Fast(500, name, "quick")
    else:
        print("Invalid choice. Defaulting to Strong.")
        return Strong(500, name, "fighty")

class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def is_alive(self):
        return self.health > 0

    def attack(self, player):
        damage = randint(1, self.damage)
        player.wound(damage)
        print(f"The {self.name} attacks {player.name} for {damage} damage!")

if __name__ == "__main__":
    print("Welcome to Whispers of Eternity: The Lost City Quest!")
    print("As an avid traveler, you have decided to visit the Whispering Woods.")
    print("Legends speak of an ancient map that reveals the location of the Lost City.")
    print("You venture into the dense forest, encountering mystical creatures and solving riddles.")
    print("Your goal is to obtain the elusive map and begin your quest.")
    print("Enter your name, hero!: ")
    name = input()
    
    player_character = select_player_class()
    player_character.name = name
    
    print(f"Good luck, {player_character.name}. You have chosen the {player_character.player_class} class.")



    
 


