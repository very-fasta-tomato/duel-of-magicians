import socket
import constructor

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

outputformat = "json"
if outputformat == "json":
    r=constructor.output(14, 20, "json")
    s.sendto(r.encode(), ('192.68.1.49', 22003))
