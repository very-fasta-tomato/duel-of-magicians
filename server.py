import socket
import CharacterClass
import SpellClass
import createObject
import constructor

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # сокет для получение IP пользователя
# AF_INET - используется IP-протокол четвертой версии. SOCK_STREAM - TCP
s.connect(("gmail.com", 80))
myIP = str(s.getsockname()[0])
s.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((myIP, 9090))
client = []  # Массив где храним адреса клиентов
print('Start Server')
while 1:
    data, addres = sock.recvfrom(1024)
    print(addres[0], addres[1])
    print(data)
    if addres not in client:
        client.append(addres)  # Если такова клиента нету , то добавить
    for clients in client:
        if clients == addres:
            sock.sendto('1'.encode(), clients)
            continue  # Не отправлять данные клиенту который их прислал
        sock.sendto(data, clients)
