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

window = sg.Window('Дуэль магов', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Выход':
        break
    if event == 'Статистика':
        event, values = sg.Window('Статистика',
                                  [[sg.Text("Победы", size=(9, 1), key='-winnum-')],
                                   [sg.Text("Поражения", size=(9, 1), key='-losenum')],
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
window.close()
