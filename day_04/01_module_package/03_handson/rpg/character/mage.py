from .character import Character

class Mage(Character):
    def attack(self, other: Character):
        damage = self._defense - other._defense
        other._health -= damage