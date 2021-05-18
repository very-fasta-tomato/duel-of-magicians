import CharacterClass
import SpellClass
import createObject
import constructor
import socket
import random
import PySimpleGUI as sg

tab1_layout = [[sg.Button('Начать игру')]]

tab2_layout = [[sg.Text('Победы:', size=(9, 1), key='-vintext-')],
               [sg.Text('Поражения:', size=(9, 1), key='-losetext-')]]

tab3_layout = [[]]

layout = [[sg.TabGroup(
    [[sg.Tab('Игра', tab1_layout), sg.Tab('Статистика', tab2_layout), sg.Tab('Настройки', tab3_layout)]],
    tooltip='TIP')]]

#layout2=[[sg.Text('Выберете режим игры', size=(19, 1))],
 #        [sg.Radio('Стандартный', 1, key=['R'])],
  #       [sg.Radio('Расширенный', 1, key=['R2'])]]

window = sg.Window('Дуэль магов', layout)

while True:
    event, values = window.read()
    #if event == "Начать игру":
       # window2=sg.Window('Режимы игры', layout2)
        #event, values=window2.read()
        #print(event, values)
        #window2.close()
    if event == sg.WIN_CLOSED:
        break
