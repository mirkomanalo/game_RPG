# Classe Base
import random

class Character():
    def __init__(self, name: str, max_hp: int, strength: int) -> None:
        self._name = name
        self._hp = max_hp
        self._strength = strength
        self._current_hp = max_hp
    
    def __str__(self) -> str:
        return f"{self._name}: [{self._current_hp}/{self._hp} - Damage: {self._strength}]"
    
    def receive_damage(self, damage: int) -> None:
        self._current_hp -= damage
        if self._current_hp < 0:
            self._current_hp = 0
    
    def is_alive(self) -> bool:
        return self._current_hp > 0
    
    def attack(self, target: "Character") -> None:
        print(f"{self._name} attacks {target._name}!")
        target.receive_damage(self._strength)
    
class Hero(Character):
    def __init__(self, name: str, max_hp: int, strength: int, potions: int) -> None:
        super().__init__(name, max_hp, strength)
        self._potions = potions

    def heal(self) -> None:
        if self._potions > 0:
            self._potions -= 1
            self._current_hp += 20
            if self._current_hp > self._hp:
                self._current_hp = self._hp
            print(f"Hero used a potion. HP: {self._current_hp}")
        else:
            print(f"No potions left")
                
class Monster(Character):
    def __init__(self, name: str, max_hp: int, strength: int) -> None:
        super().__init__(name, max_hp, strength)

    def attack(self, target: "Character") -> None:
        if random.random() < 0.25:
            double_damage = self._strength * 2
            print(f"CRITICAL HIT! {self._name} deals double damage to {target._name}!")
            target.receive_damage(double_damage)
        else:
            super().attack(target)
        
if __name__ == "__main__":
    hero_name = input("What is the Hero name? ")
    hero = Hero(hero_name, 100, 15, 2)
    monster = Monster("Goblin", 60, 10)

    print(f"Battle start")

    while hero.is_alive() and monster.is_alive():
        print(hero)
        print(monster)

        action = input(f"Press A to attack or H to heal: ")
        if action.upper() == "A":
            hero.attack(monster)
        elif action.upper() == "H":
            hero.heal()
        else:
            print("Action isn't valid. Try A or H")
            continue
        
        if monster.is_alive():
            monster.attack(hero)
            print("-" * 20)
    
    if hero.is_alive():
        print(f"Hero wins")
    else:
        print(f"Hero died")


        
        
    