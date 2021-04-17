class CharacterClass:
    def __init__(self, hp, mp):  # self - ссылка на сам объект этого класса
        self.hp = hp  # конструктор класса
        self.mp = mp

    def change_hp(self, delta_hp):  # метод изменения хп
        self.hp = self.hp + delta_hp

    def change_mp(self, delta_mp):  # метод изменения мп
        self.mp = self.mp + delta_mp
