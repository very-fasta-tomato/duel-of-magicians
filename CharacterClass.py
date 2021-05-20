class Character:
    def __init__(self, hp=20, mp=10):  # self - ссылка на сам объект этого класса
        self.hp = hp  # конструктор класса
        self.mp = mp

    def change_hp(self, delta_hp):  # метод изменения хп
        self.hp = self.hp - delta_hp

    def change_mp(self, delta_mp):  # метод изменения мп
        self.mp = self.mp - delta_mp
        if self.mp < 0:  # защита от ухода маны в -
            self.mp = 0

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def set_hp(self, hp):
        self.hp = hp

    def set_mp(self, mp):
        self.mp = mp

    def death_check(self):  # проверка смерти
        if self.hp < 0 or self.hp == 0:
            return True
        else:
            return False
