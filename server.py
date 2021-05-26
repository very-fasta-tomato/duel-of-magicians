import socket
import CharacterClass
import SpellClass
import createObject
import constructor


def launch_game(sock, clients):
    player1 = CharacterClass.Character()
    player2 = CharacterClass.Character()
    #  начало игры
    round_of_game = 0
    while True:
        round_of_game += 1
        if round_of_game % 2 == 0:
            _data, _addr = sock.recvfrom(1024)
            if _addr == clients[0]:
                player1_spell1 = createObject.createclassic()
                player1_spell2 = createObject.createclassic()
                player1_spell3 = createObject.createclassic()
                if _data == 'Заклинание 1':
                    player1.change_hp(player1_spell1.get_delta_ally_hp())
                    player1.change_mp(player1_spell1.get_delta_ally_mp())
                    player2.change_hp(player1_spell1.get_delta_ally_hp())
                    player2.change_mp(player1_spell1.get_delta_ally_mp())
                if _data == 'Заклинание 2':
                    player1.change_hp(player1_spell2.get_delta_ally_hp())
                    player1.change_mp(player1_spell2.get_delta_ally_mp())
                    player2.change_hp(player1_spell2.get_delta_ally_hp())
                    player2.change_mp(player1_spell2.get_delta_ally_mp())
                if _data == 'Заклинание 3':
                    player1.change_hp(player1_spell3.get_delta_ally_hp())
                    player1.change_mp(player1_spell3.get_delta_ally_mp())
                    player2.change_hp(player1_spell3.get_delta_ally_hp())
                    player2.change_mp(player1_spell3.get_delta_ally_mp())
        else:
            _data, _addr = sock.recvfrom(1024)
            if _addr == clients[1]:
                player2_spell1 = createObject.createclassic()
                player2_spell2 = createObject.createclassic()
                player2_spell3 = createObject.createclassic()
                if _data == 'Заклинание 1':
                    player1.change_hp(player2_spell1.get_delta_ally_hp())
                    player1.change_mp(player2_spell1.get_delta_ally_mp())
                    player2.change_hp(player2_spell1.get_delta_ally_hp())
                    player2.change_mp(player2_spell1.get_delta_ally_mp())
                if _data == 'Заклинание 2':
                    player1.change_hp(player2_spell2.get_delta_ally_hp())
                    player1.change_mp(player2_spell2.get_delta_ally_mp())
                    player2.change_hp(player2_spell2.get_delta_ally_hp())
                    player2.change_mp(player2_spell2.get_delta_ally_mp())
                if _data == 'Заклинание 3':
                    player1.change_hp(player2_spell3.get_delta_ally_hp())
                    player1.change_mp(player2_spell3.get_delta_ally_mp())
                    player2.change_hp(player2_spell3.get_delta_ally_hp())
                    player2.change_mp(player2_spell3.get_delta_ally_mp())


clients = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", 14900))
sock.listen(2)  # максимальное число соединений в очереди
while True:
    data, addr = sock.recvfrom(1024)
    if addr not in clients:
        clients.append(addr)
    if len(clients) == 2:
        launch_game(sock, clients)
