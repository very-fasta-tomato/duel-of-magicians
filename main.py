import json
import CharacterClass
import createObject
import constructor
import socket
import SpellClass
import PySimpleGUI as sg  # сторонний GUI фреймворк


def screenupdate():
    window2['-hp-'].Update(str(player.get_hp()))
    window2['-mp-'].Update(str(player.get_mp()))
    window2['-deh1-'].Update(str(spell1.delta_enemy_hp))
    window2['-deh2-'].Update(str(spell2.delta_enemy_hp))
    window2['-deh3-'].Update(str(spell3.delta_enemy_hp))
    window2['-dam1-'].Update(str(spell1.delta_ally_mp))
    window2['-dam2-'].Update(str(spell2.delta_ally_mp))
    window2['-dam3-'].Update(str(spell3.delta_ally_mp))
    window2['-dem1-'].Update(str(spell1.delta_enemy_mp))
    window2['-dem2-'].Update(str(spell2.delta_enemy_mp))
    window2['-dem3-'].Update(str(spell3.delta_enemy_mp))
    window2['-dah1-'].Update(str(spell1.delta_ally_hp * (-1)))
    window2['-dah2-'].Update(str(spell2.delta_ally_hp * (-1)))
    window2['-dah3-'].Update(str(spell3.delta_ally_hp * (-1)))
    window2['-vp1-'].Update(str(spell1.verojatnost_popadanija))
    window2['-vp2-'].Update(str(spell2.verojatnost_popadanija))
    window2['-vp3-'].Update(str(spell3.verojatnost_popadanija))


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # сокет для получение IP пользователя
# AF_INET - используется IP-протокол четвертой версии. SOCK_STREAM - TCP
s.connect(("gmail.com", 80))
myIP = str(s.getsockname()[0])
s.close()
s_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # сокет для получения данных
s_in.bind((myIP, 22003))  # резерв адреса myIP и порта 22003
s_in.listen(1)
s_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # сокет для отправки данных
pvevent = ''
winstat = 0
losestat = 0
enemyturn = ''

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
        event, values = sg.Window('Режимы игры',
                                  [[sg.Text('Выберете режим игры')],
                                   [sg.Button('Стандартный', size=(11, 1))],
                                   [sg.Button('Расширенный', size=(11, 1))]]).read(close=True)
        spell1 = SpellClass.Spell(0, 0, 0, 0, 0)
        spell2 = SpellClass.Spell(0, 0, 0, 0, 0)
        spell3 = SpellClass.Spell(0, 0, 0, 0, 0)
        if event == 'Стандартный':
            spell1 = createObject.createclassic()
            spell2 = createObject.createclassic()
            spell3 = createObject.createclassic()
            pvevent = 'Стандартный'
        if event == 'Расширенный':
            spell1 = createObject.createmaximum()
            spell2 = createObject.createmaximum()
            spell3 = createObject.createmaximum()
            pvevent = 'Расширенный'
        print(event, values)
        event, values = sg.Window('Поиск оппонента',
                                  [[sg.Text('Введите IP оппонента')],
                                   [sg.Input(key='-IP-')],
                                   [sg.Button('OK')]]).read(close=True)
        print(event, values)
        IP = values['-IP-']
        print(IP, myIP)
        if myIP > IP:
            enemyturn = False
        player = CharacterClass.Character()
        print(player.get_hp())
        s_out.connect((IP, 22003))
        window2 = sg.Window('game', layout2)  # объявление окна с полем
        wn2 = True
        while wn2:
            event, values = window2.read()  # создание окна с полем
            screenupdate()
            if event == sg.WIN_CLOSED:
                wn2 = False
            if event == 'Заклинание 1':
                if not enemyturn:
                    player.change_hp(spell1.delta_ally_hp)
                    player.change_mp(spell1.delta_ally_mp)
                    r = constructor.output(spell1.delta_enemy_hp, spell1.delta_enemy_mp, "json")
                    s_out.send(r.encode())
                    spell1 = SpellClass.Spell(0, 0, 0, 0, 0)
                    spell2 = SpellClass.Spell(0, 0, 0, 0, 0)
                    spell3 = SpellClass.Spell(0, 0, 0, 0, 0)
                data = b""
                s_in.settimeout(60)
                client, addr = s_in.accept()
                result = client.recv(1024)
                g = json.loads(result.decode())
                window2['TURN'].Update('Сейчас ход оппонента')
                player.change_hp(g.get('delta_enemy_hp'))
                player.change_mp(g.get('delta_enemy_mp'))
            if event == 'Заклинание 2':
                if not enemyturn:
                    player.change_hp(spell2.delta_ally_hp)
                    player.change_mp(spell2.delta_ally_mp)
                    r = constructor.output(spell2.delta_enemy_hp, spell2.delta_enemy_mp, "json")
                    s_out.send(r.encode())
                    spell1 = SpellClass.Spell(0, 0, 0, 0, 0)
                    spell2 = SpellClass.Spell(0, 0, 0, 0, 0)
                    spell3 = SpellClass.Spell(0, 0, 0, 0, 0)
                data = b""
                s_in.settimeout(60)
                client, addr = s_in.accept()
                result = client.recv(1024)
                g = json.loads(result.decode())
                window2['TURN'].Update('Сейчас ход оппонента')
                player.change_hp(g.get('delta_enemy_hp'))
                player.change_mp(g.get('delta_enemy_mp'))
            if event == 'Заклинание 3':
                if not enemyturn:
                    player.change_hp(spell3.delta_ally_hp)
                    player.change_mp(spell3.delta_ally_mp)
                    r = constructor.output(spell3.delta_enemy_hp, spell3.delta_enemy_mp, "json")
                    s_out.send(r.encode())
                    spell1 = SpellClass.Spell(0, 0, 0, 0, 0)
                    spell2 = SpellClass.Spell(0, 0, 0, 0, 0)
                    spell3 = SpellClass.Spell(0, 0, 0, 0, 0)
                data = b""
                s_in.settimeout(60)
                client, addr = s_in.accept()
                result = client.recv(1024)
                g = json.loads(result.decode())
                window2['TURN'].Update('Сейчас ход оппонента')
                player.change_hp(g.get('delta_enemy_hp'))
                player.change_mp(g.get('delta_enemy_mp'))
        window2.close()
        s_out.close()
        s_in.close()
window.close()
