import socket
import json
import time

host = '127.0.0.1'
port = 2002
address = (host,port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect((host, port))
f = open("help.json")

send_msg = f.read(14)
while send_msg:
        s.send(send_msg)
        time.sleep(.2)
        send_msg = f.read()
print json.loads(s.recv(1024))
