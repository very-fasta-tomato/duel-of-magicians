import CharacterClass
import createObject
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

root = Tk()


def startgame(selected):
    player = CharacterClass.Character()
    if selected.get() == 1:
        spell1 = createObject.createclassic()
        spell2 = createObject.createclassic()
        spell3 = createObject.createclassic()
    if selected.get() == 2:
        spell1=createObject.createmaximum()
        spell2 = createObject.createmaximum()
        spell3 = createObject.createmaximum()



def command():
    window2 = Toplevel(root)
    window2.title("Режимы игры")
    window2.geometry('450x450')
    lbl = Label(window2, text="Выберите режим игры")
    lbl.grid(column=0, row=1)
    selected = IntVar()
    rad1 = Radiobutton(window2, text='Традиционный', value=1, variable=selected)
    rad2 = Radiobutton(window2, text='Нетрадиционный', value=2, variable=selected)
    rad1.grid(column=0, row=3)
    rad2.grid(column=1, row=3)
    btn21 = Button(window2, text="Начать игру")
    btn21.grid(column=0, row=2)
    window2.mainloop()


root.title("Битва магов")
root.geometry('600x600')
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Игра')
tab_control.add(tab2, text='Статистика')
tab_control.add(tab3, text='Настройки')
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(tab3, text='Включить звук', var=chk_state)
chk.grid(column=0, row=0)
btn11 = Button(tab1, text="Начать игру", command=command)
btn11.grid(column=1, row=0)
btn12 = Button(tab1, text="Выход", command=root.quit)
btn12.grid(column=1, row=2)
tab_control.pack(expand=1, fill='both')

root.mainloop()
