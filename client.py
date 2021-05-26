import socket
import json
import constructor
import PySimpleGUI as sg  # сторонний GUI фреймворк

winstat = 0
losestat = 0
conn = socket.socket()

layout = [[sg.Button('Начать игру', size=(11, 1))],  # структура главного окна
          [sg.Button('Статистика', size=(11, 1))],
          [sg.Button('Настройки', size=(11, 1))],
          [sg.Button('Выход', size=(11, 1))]]

layout2 = [[sg.Text('Сейчас ваш ход', key='TURN')],  # структура окна игры
           [sg.Text('Ваши HP', key='-hp-')],
           [sg.Text('Ваши MP', key='-mp-')],
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
            sg.Text('Вероятность попадания', key='-vp3-', size=(21, 1))],
           [sg.Button('Обновить данные')]]

window = sg.Window('Дуэль магов', layout)  # объявление главного окна
while True:
    event, values = window.read()  # создание главного окна
    if event == sg.WIN_CLOSED or event == 'Выход':
        break
    if event == 'Статистика':
        event, values = sg.Window('Статистика',
                                  [[sg.Text("Победы", size=(9, 1)), sg.Text(str(winstat))],
                                   [sg.Text("Поражения", size=(9, 1)), sg.Text(str(losestat))],
                                   [sg.Button('Назад')]]).read(close=True)
        print(event, values)
    if event == 'Настройки':
        event, values = sg.Window('Настройки',
                                  [[sg.Checkbox('Включить звук', enable_events=True, key='-sound-')],
                                   [sg.Button('Назад')]]).read(close=True)
        print(event, values)
    if event == 'Начать игру':
        event, values = sg.Window('Поиск оппонента',
                                  [[sg.Text('Введите IP сервера')],
                                   [sg.Input(key='-IP-')],
                                   [sg.Button('OK')]]).read(close=True)
        IP = values['-IP-']
        conn.connect((IP, 14900))
        event, values = sg.Window('Режимы игры',
                                  [[sg.Text('Выберете режим игры')],
                                   [sg.Button('Стандартный', size=(11, 1))],
                                   [sg.Button('Расширенный', size=(11, 1))]]).read(close=True)
        if event == 'Стандартный':
            conn.send(json.dumps('Стандартный').encode())
        if event == 'Расширенный':
            conn.send(json.dumps('Расширенный').encode())
        window2 = sg.Window('game', layout2)  # объявление окна с полем
        wn2 = True
        while wn2:
            event, values = window2.read()  # создание окна с полем
            if event == sg.WIN_CLOSED:
                wn2 = False
            if event == 'Заклинание 1':
                conn.send(json.dumps('Заклинание 1').encode())
            if event == 'Заклинание 2':
                conn.send(json.dumps('Заклинание 2').encode())
            if event == 'Заклинание 3':
                conn.send(json.dumps('Заклинание 3').encode())
