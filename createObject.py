import SpellClass
import random


def createclassic():
    delta_enemy_hp = random.randint(1, 7)
    delta_ally_mp = random.randint(1, 2)
    spell1 = SpellClass.Spell(delta_enemy_hp, 0, 0, delta_ally_mp, 0)
    return spell1


def createmaximum():
    delta_enemy_hp = random.randint(-2, 7)
    delta_ally_mp = random.randint(-2, 2)
    delta_enemy_mp = random.randint(-2, 1)
    delta_ally_hp = random.randint(-2, 1)
    spell1 = SpellClass.Spell(delta_enemy_hp, delta_enemy_mp, delta_ally_hp, delta_ally_mp, 0)
    return spell1


createclassic()
