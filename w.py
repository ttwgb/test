import socket
d=('192.168.3.255',9)
p='\xff'*6+'\x40\xf2\xe9\xd6\x03\xc4'*16

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(p,d)
#A4 1F 72 59 D4 13

