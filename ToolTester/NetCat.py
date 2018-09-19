#!/bin/usr/python3
import socket
import random
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = random.randint(4000,6000)
some_data = b'\xff\xfeF\x00L\x00A\x00G\x00{\x00n\x00e\x00T\x00C\x00a\x00t\x00_\x00i\x00S\x00_\x00F\x00u\x00N\x00_\x00t\x00o\x00_\x00p\x00L\x00a\x00Y\x00_\x00w\x00i\x00T\x00H\x00}\x00'
print(" Target is {} \n Go Get the Flag.. \n\n".format(port))
sock.bind(('127.0.0.1',port))
sock.listen(1)
conn , addr = sock.accept()
conn.send("\033[2J \033[HOnly the Worthy ones shall pass. \n".encode())
data = conn.recv(1024)
if(data.decode().lower().find('please')!=-1):
    conn.send("\nok. Flag is {} \n \n".format(some_data.decode('utf-16')).encode())
else:
    conn.send("\nYou should have atleast requested ... \n".encode())

conn.send("\nCtrl+C to Exit . Code is Exiting .. \n".encode())
conn.close()
sock.close()
