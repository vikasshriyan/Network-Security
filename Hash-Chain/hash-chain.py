import crypt
import json
import string
with open("/home/hash-chain/table.json") as json_file:
        json_data = json.load(json_file)
        hash_chains = json_data['chains']

def MD5(plain_text):
         return crypt.crypt(plain_text,'$1$HUSKIES!$')


def reduce(hash_result):
        tmp = hash_result[-8:]
        result = ""
        for i in tmp[::-1]:
                result += chr(ord(i)%26 + ord('a'))
        return result

hash_result = raw_input("enter the hash")


value = reduce(hash_result)
s=0
k=0
while s<1:
        print(k)
        for chain in hash_chains:

                if value == chain['end']:
                        start = chain['start']
                        print chain['start']
                        print chain['end']
                        s+=1
                        break
                else:
                        s=0

        tmp = MD5(value)
        value=reduce(tmp)
        k+=1
hash_tmp=MD5(start)
while hash_result != hash_tmp:
        password_c= reduce(hash_tmp)
        hash_tmp = MD5(password_c)
print password_c
