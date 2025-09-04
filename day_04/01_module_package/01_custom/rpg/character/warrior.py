from .character import Character


class Warrior(Character):
    def __init__(self, health=10, defense=10, strength=10):
        super().__init__(health, defense)
        self._strength = strength

    def attack(self, other: Character):
        damage = self._strength - other._defense
        other._health -= damage
