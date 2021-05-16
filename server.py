import socket
import json

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# AF_INET - используется IP-протокол четвертой версии. SOCK_DGRAMM - UDP
s.bind(('127.0.0.1', 8888))  # резерв адреса 127.0.0.1 и порта 8888
brk = True
while 1:
    result = s.recv(1024)  # прослушка порта и получение данных по одному килобайту
    print('Message:', result.decode())
    if brk:
        break
# g=json.loads(result.decode())
# print(g.get('delta_enemy_hp'))
s.close()  # остановка прослушиваение порта и его освобождение
