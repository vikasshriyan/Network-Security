import json
import socket
import base64
import struct
from Crypto.Cipher import ARC4
#connect with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',5452))

#step1: send the init msg to S
f = open("needham-help.json")
init_value = f.read()
s.sendall(struct.pack('>I', len(init_value)))
s.sendall(init_value)
#Ka,s
secret_AU_C = '\xeb\xb0\x18\xbd\xa2\x09\xde\xbb\xc4\x5e\x77\x00\xdc\x0e\x99\xb5'
#step2: decrypt the msg from S
l = struct.unpack('>I', s.recv(4))[0]
buf = s.recv(l)
enc = ARC4.new(secret_AU_C)
msg = json.loads(enc.encrypt(buf))

#step3: send the blob to B
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect(('127.0.0.1',5453))
blob = base64.b64decode(msg["blob"])

s1.sendall(struct.pack('>I', len(blob)))
s1.sendall(blob)
#step4: decrypt the msg from B
l = struct.unpack('>I', s1.recv(4))[0]
buf = s1.recv(l)
enc = ARC4.new(base64.b64decode(msg['session_key']))
msg = json.loads(enc.decrypt(buf))
#final step: send the nonce-- to B
msg1 = enc.encrypt(json.dumps({"nonce": msg['nonce'] - 1}))
s1.sendall(struct.pack('>I',len(msg1)))
s1.sendall(msg1)
#recieve the secret
l = struct.unpack('>I',s1.recv(4))[0]
buf = s1.recv(l)
msg = json.loads(enc.decrypt(buf))
print msg
