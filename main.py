import CharacterClass
import createObject
import SpellClass
from tkinter import*
from tkinter import ttk
from tkinter.ttk import*



window = Tk()
window.title("Битва магов")
window.geometry('600x600')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Игра', )
tab_control.add(tab2, text='Статистика')
tab_control.add(tab3, text='Настройки')
chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(tab3, text='Включить звук', var=chk_state)
chk.grid(column=0, row=0)
btn11 = Button(tab1, text="Начать игру")
btn11.grid(column=1, row=0)
btn12 = Button(tab1, text="Выход", command=window.quit)
btn12.grid(column=1, row=2)
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')
window.mainloop()
