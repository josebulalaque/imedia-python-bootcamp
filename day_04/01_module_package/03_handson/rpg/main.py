from character.knight import Knight
from character.mage import Mage
from character.warrior import Warrior

knight1 = Knight(100,50)
warrior1 = Warrior(100,30)
mage1 = Mage(100,10)

knight1.attack(warrior1)
print(knight1.show_health())
print(warrior1.show_health())