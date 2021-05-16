import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# AF_INET - используется IP-протокол четвертой версии. SOCK_DGRAMM - UDP
s.bind(('127.0.0.1', 8888))
result = s.recv(1024)
print('Message:', result.decode('utf-8'))
s.close()
