#!/bin/usr/python2
import subprocess

some_data = b'\xff\xfeF\x00L\x00A\x00G\x00{\x00m\x00A\x00c\x00_\x00A\x00d\x00d\x00r\x00r\x00e\x00s\x00S\x00_\x00c\x00A\x00N\x00_\x00B\x00e\x00_\x00c\x00o\x00o\x00L\x00_\x00t\x00O\x00_\x00P\x00L\x00a\x00y\x00_\x00W\x00i\x00t\x00H\x00}\x00'
target    = "00:49:A3:F8:71:FE"
data =  subprocess.Popen("ifconfig", shell=True, stdout=subprocess.PIPE).stdout.read()
if(data.upper().find(target.encode()) != -1 ):
    print(some_data.decode('utf-16'))
else:
    print("Nah..")