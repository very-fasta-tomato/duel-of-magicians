import CharacterClass
import createObject
import tkinter as tk
import constructor
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.colorchooser import askcolor

root = Tk()  # главное окно


def startgame(selected):
    player = CharacterClass.Character()
    if selected == 1:
        spell1 = createObject.createclassic()
        spell2 = createObject.createclassic()
        spell3 = createObject.createclassic()
    if selected == 2:
        spell1 = createObject.createmaximum()
        spell2 = createObject.createmaximum()
        spell3 = createObject.createmaximum()
    windowGame = Toplevel()
    windowGame.title("Битва магов")
    windowGame.geometry('700x700')
    lbl341 = Label(windowGame, text='Ваше XP:')
    lbl341.grid(column=6, row=0)
    lb3411 = Label(windowGame, text='')
    lb3411.grid(column=7, row=0)  # техническое поле
    lbl342 = Label(windowGame, text='Ваша мана:')
    lbl342.grid(column=8, row=0)
    lb3421 = Label(windowGame, text='')
    lb3421.grid(column=9, row=0)  # техническое поле
    btn31 = Button(windowGame, text="Заклинание 1")
    btn31.grid(column=0, row=0)
    lb3101 = Label(windowGame, text='')
    lb3101.grid(column=1, row=0)  # техническое поле
    lbl311 = Label(windowGame, text='Урон:')
    lbl311.grid(column=0, row=1)
    lb3111 = Label(windowGame, text='')
    lb3111.grid(column=1, row=1)  # техническое поле
    lbl312 = Label(windowGame, text='Мана:')
    lbl312.grid(column=0, row=2)
    lb3121 = Label(windowGame, text='')
    lb3121.grid(column=1, row=2)  # техническое поле
    lbl313 = Label(windowGame, text='урон мане:')
    lbl313.grid(column=0, row=3)
    lb3131 = Label(windowGame, text='')
    lb3131.grid(column=1, row=3)  # техническое поле
    lbl314 = Label(windowGame, text='восстановление хп:')
    lbl314.grid(column=0, row=4)
    lb3141 = Label(windowGame, text='')
    lb3141.grid(column=1, row=4)  # техническое поле
    lbl315 = Label(windowGame, text='вероятность попадания:')
    lbl315.grid(column=0, row=5)
    lb3151 = Label(windowGame, text='')
    lb3151.grid(column=1, row=5)  # техническое поле
    btn32 = Button(windowGame, text="Заклинание 2")
    btn32.grid(column=2, row=0)
    lb3201 = Label(windowGame, text='')
    lb3201.grid(column=3, row=0)  # техническое поле
    lbl321 = Label(windowGame, text='Урон:')
    lbl321.grid(column=2, row=1)
    lb3211 = Label(windowGame, text='')
    lb3211.grid(column=3, row=1)  # техническое поле
    lbl322 = Label(windowGame, text='Мана:')
    lbl322.grid(column=2, row=2)
    lb3221 = Label(windowGame, text='')
    lb3221.grid(column=3, row=2)  # техническое поле
    lbl323 = Label(windowGame, text='урон мане:')
    lbl323.grid(column=2, row=3)
    lb3231 = Label(windowGame, text='')
    lb3231.grid(column=3, row=3)  # техническое поле
    lbl324 = Label(windowGame, text='восстановление хп:')
    lbl324.grid(column=2, row=4)
    lb3241 = Label(windowGame, text='')
    lb3241.grid(column=3, row=4)  # техническое поле
    lbl325 = Label(windowGame, text='вероятность попадания:')
    lbl325.grid(column=2, row=5)
    lb3251 = Label(windowGame, text='')
    lb3251.grid(column=3, row=5)  # техническое поле
    btn33 = Button(windowGame, text="Заклинание 3")
    btn33.grid(column=4, row=0)
    lb3301 = Label(windowGame, text='')
    lb3301.grid(column=5, row=0)  # техническое поле
    lbl331 = Label(windowGame, text='Урон:')
    lbl331.grid(column=4, row=1)
    lb3311 = Label(windowGame, text='')
    lb3311.grid(column=5, row=1)  # техническое поле
    lbl332 = Label(windowGame, text='Мана:')
    lbl332.grid(column=4, row=2)
    lb3321 = Label(windowGame, text='')
    lb3321.grid(column=5, row=2)  # техническое поле
    lbl333 = Label(windowGame, text='урон мане:')
    lbl333.grid(column=4, row=3)
    lb3331 = Label(windowGame, text='')
    lb3331.grid(column=5, row=3)  # техническое поле
    lbl334 = Label(windowGame, text='восстановление хп:')
    lbl334.grid(column=4, row=4)
    lb3341 = Label(windowGame, text='')
    lb3341.grid(column=5, row=4)  # техническое поле
    lbl335 = Label(windowGame, text='вероятность попадания:')
    lbl335.grid(column=4, row=5)
    lb3351 = Label(windowGame, text='')
    lb3351.grid(column=5, row=5)  # техническое поле


    def cast(spell, ):
        player.change_hp(spell.delta_ally_hp)
        player.change_mp(spell.delta_ally_mp)
        constructor.output(spell.delta_enemy_hp, spell.delta_enemy_mp, "json")


def command():
    window1 = tk.Toplevel(root)

    def createButton():
        btn21 = Button(window1, text="Начать игру", command=startgame(selected))  # запуск основного кода
        btn21.grid(column=1, row=3)

    window1.title("Режимы игры")
    window1.geometry('450x450')
    lbl = Label(window1, text="Выберите режим игры")
    lbl.grid(column=0, row=1)
    selected = IntVar()
    rad1 = Radiobutton(window1, text='Традиционный', value=1, variable=selected, command=createButton)
    rad2 = Radiobutton(window1, text='Нетрадиционный', value=2, variable=selected, command=createButton)

    rad1.grid(column=0, row=2)
    rad2.grid(column=1, row=2)

    btn22 = Button(window1, text="Назад", command=window1.quit)

    btn22.grid(column=0, row=3)
    window1.mainloop()


root.title("Битва магов")
root.geometry('600x600')
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Игра')
tab_control.add(tab2, text='Статистика')
lbl1 = Label(tab2, text="Победы")
lbl1.grid(column=0, row=1)
lbl2 = Label(tab2, text="Поражения")
lbl2.grid(column=2, row=1)
tab_control.add(tab3, text='Настройки')
chk_state = BooleanVar()
chk_state.set(True)
chk1 = Checkbutton(tab3, text='Включить звук', var=chk_state)
chk1.grid(column=0, row=0)
btn11 = Button(tab1, text="Начать игру", command=command)  # открывается окно с выбором режимов
btn11.grid(column=1, row=0)
btn12 = Button(tab1, text="Выход", command=root.quit)
btn12.grid(column=1, row=2)
tab_control.pack(expand=1, fill='both')
root.mainloop()
