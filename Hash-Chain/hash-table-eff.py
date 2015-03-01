import json
import crypt
import io
def MD5(plain_text):
         return crypt.crypt(plain_text.encode('utf8'),'$1$HUSKIES!$')


def reduce(hash_result):
        tmp = hash_result[-8:]
        result = ""
        for i in tmp[::-1]:
                result += chr(ord(i)%26 + ord('a'))
        return result

with open("/home/hash-chain/table.json") as f:
        table = json.loads(f.read())
        #print table['chains']

name_space = set()
print name_space
for chain in table['chains']:
        value = chain['start']
        name_space.add(value)
        while value != chain['end']:
                value = reduce(MD5(value))
                name_space.add(value)
                print len(name_space)

length = len(name_space)
result = length/(128*65536)

print result

