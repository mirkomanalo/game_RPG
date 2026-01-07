# Classe Base

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
                
    
        
    