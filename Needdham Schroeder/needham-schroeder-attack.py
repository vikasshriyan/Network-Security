import base64
import json
import socket
import struct
from Crypto.Cipher import ARC4

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5453))
f = open("/home/network-auth/blob")
blob = f.read()

f1 = open("/home/network-auth/key")
key = f1.read()
s.sendall(struct.pack('>I', len(blob)))
s.sendall(blob)

l = struct.unpack('>I', s.recv(4))[0]
buf = s.recv(l)
enc = ARC4.new(key)
msg = json.loads(enc.encrypt(buf))

msg1 = enc.encrypt(json.dumps({"nonce": msg['nonce'] - 1}))
s.sendall(struct.pack('>I',len(msg1)))
s.sendall(msg1)
#recieve the secret
l = struct.unpack('>I',s.recv(4))[0]
buf = s.recv(l)
msg = json.loads(enc.decrypt(buf))
print msg


