import CharacterClass
import createObject
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.colorchooser import askcolor

root = Tk() # главное окно


def startgame(selected):
    windowgame = Tk()
    windowgame.title("Битва магов")
    windowgame.geometry('700x700')
    lbl31 = Label(windowgame, text = 'Мана')
    lbl31.grid(column=0, row=1)
    lbl31 = Label(windowgame, text='XP')
    lbl31.grid(column=1, row=1)
    btn31 = Button(windowgame, text = "Заклинание 1")
    btn31.grid(column=0, row=0)
    btn32 = Button(windowgame, text = "Заклинание 2")
    btn32.grid(column=1, row=0)
    btn33 = Button(windowgame, text = "Заклинание 3")
    btn33.grid(column=2, row=0)

    player = CharacterClass.Character()
    if selected == 1:
        spell1 = createObject.createclassic()
        spell2 = createObject.createclassic()
        spell3 = createObject.createclassic()
    if selected == 2:
        spell1=createObject.createmaximum()
        spell2 = createObject.createmaximum()
        spell3 = createObject.createmaximum()





def command():
    window1 = tk.Toplevel(root)

    def createButton():
        btn21 = Button(window1, text="Начать игру", command=startgame(selected)) # запуск основного кода
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
lbl1 = Label (tab2, text="Победы")
lbl1.grid(column=0, row=1)
lbl2 = Label (tab2, text="Поражения")
lbl2.grid(column=2, row=1)
tab_control.add(tab3, text='Настройки')
chk_state = BooleanVar()
chk_state.set(True)
chk1 = Checkbutton(tab3, text='Включить звук', var=chk_state)
chk1.grid(column=0, row=0)
btn11 = Button(tab1, text="Начать игру", command=command) # открывается окно с выбором режимов
btn11.grid(column=1, row=0)
btn12 = Button(tab1, text="Выход", command=root.quit)
btn12.grid(column=1, row=2)
tab_control.pack(expand=1, fill='both')
root.mainloop()
