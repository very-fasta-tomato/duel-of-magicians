import CharacterClass
import createObject
import SpellClass
from tkinter import*



window = Tk()
window.title("Битва магов")
window.geometry('600x600')
lbl = Label(window, text = "Битва Магов")
lbl.grid(column = 1, row = 0)
#btn1 = Button(window, text = "Начать игру")
#btn1.grid(column = 2, row = 5)
#btn2 = Button(window, text = "Выход", command = window.destroy())
#btn2.grid(column = 5, row = 9)
#btn3 = Button(window, text = "Статистика")
#btn3.grid(column = 5, row = 6)
#btn4 = Button(window, text = "Настройки")
#btn4.grid(column = 5, row = 7)
window.mainloop()
