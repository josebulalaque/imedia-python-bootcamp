from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, health=10, defense=10):
        self._health = health
        self._defense = defense

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()

    def show_health(self):
        return self._health

class Knight(Character):
    def attack(self, other: Character):
        damage = self._defense - other._defense
        other._health -= damage

class Mage(Character):
    def attack(self, other: Character):
        damage = self._defense - other._defense
        other._health -= damage

class Warrior(Character):
    def attack(self, other: Character):
        damage = self._defense - other._defense
        other._health -= damage


knight1 = Knight(100,50)
warrior1 = Warrior(100,30)
mage1 = Mage(100,10)

knight1.attack(warrior1)
print(knight1.show_health())
print(warrior1.show_health())
