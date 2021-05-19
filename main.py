import CharacterClass
import SpellClass
import createObject
import constructor
import socket
import random
import PySimpleGUI as sg  # сторонний GUI фреймворк

layout = [[sg.Button('Начать игру', size=(11, 1))],  # структура главного окна
          [sg.Button('Статистика', size=(11, 1))],
          [sg.Button('Настройки', size=(11, 1))],
          [sg.Button('Выход', size=(11, 1))]]
layout2 = [[sg.Text('Сейчас ваш ход', key='TURN')],  # структура окна игры
           [sg.Text('Ваше HP', key='-hp-')],
           [sg.Text('Ваше MP', key='-mp-')],
           [sg.Button('Заклинание 1', size=(21, 1)), sg.Button('Заклинание 2', size=(21, 1)),
            sg.Button('Заклинание 3', size=(21, 1))],
           [sg.Text('Урон', key='-deh1-', size=(21, 1)), sg.Text('Урон', key='-deh2-', size=(21, 1)),
            sg.Text('Урон', key='-deh3-', size=(21, 1))],
           [sg.Text('Стоимость', key='-dam1-', size=(21, 1)), sg.Text('Стоимость', key='-dam2-', size=(21, 1)),
            sg.Text('Стоимость', key='-dam3-', size=(21, 1))],
           [sg.Text('Урон мане', key='-dem1-', size=(21, 1)), sg.Text('Урон мане', key='-dem2-', size=(21, 1)),
            sg.Text('Урон мане', key='-dem3-', size=(21, 1))],
           [sg.Text('Восстановление HP', key='-dah1-', size=(21, 1)),
            sg.Text('Восстановление HP', key='-dah2-', size=(21, 1)),
            sg.Text('Восстановление HP', key='-dah3-', size=(21, 1))],
           [sg.Text('Вероятность попадания', key='-vp1-', size=(21, 1)),
            sg.Text('Вероятность попадания', key='-vp2-', size=(21, 1)),
            sg.Text('Вероятность попадания', key='-vp3-', size=(21, 1))]]

window = sg.Window('Дуэль магов', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Выход':
        break
    if event == 'Статистика':
        event, values = sg.Window('Статистика',
                                  [[sg.Text("Победы", key='-winnum-')],
                                   [sg.Text("Поражения", key='-losenum-')],
                                   [sg.Button('Назад')]]).read(close=True)
        print(event, values)
    if event == 'Настройки':
        event, values = sg.Window('Настройки',
                                  [[sg.Checkbox('Включить звук', enable_events=True, key='-sound-')],
                                   [sg.Button('Назад')]]).read(close=True)
        print(event, values)
    if event == 'Начать игру':
        event, values = sg.Window('Режимы игры',
                                  [[sg.Text('Выберете режим игры')],
                                   [sg.Button('Стандартный', size=(11, 1))],
                                   [sg.Button('Расширенный', size=(11, 1))]]).read(close=True)
        print(event, values)
        event, values = sg.Window('Поиск оппонента',
                                  [[sg.Text('Введите IP оппонента')],
                                   [sg.Input(key='-IP-')],
                                   [sg.Text('Введите ваш IP')],
                                   [sg.Input(key='-myIP-')],
                                   [sg.Button('OK')]]).read(close=True)
        print(event, values)
        IP = values['-IP-']
        myIP = values['-myIP-']
        print(IP, myIP)
        player = CharacterClass.Character()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # AF_INET - используется IP-протокол четвертой версии. SOCK_DGRAMM - UDP
        s.bind((myIP, 22003))  # резерв адреса myIP и порта 22003
        window2 = sg.Window('game', layout2)
        wn2 = True
        while wn2:
            event, values = window2.read()
            if event == sg.WIN_CLOSED:
                wn2 = False
window.close()
