import socket
import constructor

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
outputformat = "json"
if outputformat == "json":
    r=constructor.output(14, 20, "json")
    s.sendto('json'.encode(), ('127.0.0.1', 8888))
    s.sendto(r.encode(), ('127.0.0.1', 8888))
