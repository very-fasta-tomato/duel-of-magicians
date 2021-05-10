class Spell:
    def __init__(self, delta_enemy_hp, delta_enemy_mp, delta_ally_hp, delta_ally_mp, verojatnost_popadanija):
        self.delta_enemy_hp = delta_enemy_hp  # урон врагу
        self.delta_enemy_mp = delta_enemy_mp  # урон мане врага
        self.delta_ally_hp = delta_ally_hp  # урон себе
        self.delta_ally_mp = delta_ally_mp  # потребление маны
        self.verojatnost_popadanija = verojatnost_popadanija

    def get_delta_enemy_hp(self):
        return self.delta_enemy_hp

    def get_delta_enemy_mp(self):
        return self.delta_enemy_mp

    def get_delta_ally_hp(self):
        return self.delta_ally_hp

    def get_delta_ally_mp(self):
        return self.delta_ally_mp

    def get_verojatnost_popadanija(self):
        return self.verojatnost_popadanija
