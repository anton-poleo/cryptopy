import base64
from base64 import b64encode, b64decode
import binascii
def encode_to_base(str):
    str.encode('utf-8')
    str_base = binascii.a2b_hex(str)

    return str_base
def base_to_str(ptr):
    str = binascii.b2a_hex(ptr)
    str = str.decode('utf-8')
    return str


def xor(str1, str2):
    #print(str1)
    #print(str2)
    if(len(str1)!=len(str2)):
        #print(str1)
        #print(str2)
        print("Массивы не совпадают")
        return
    else:
        str1 = encode_to_base(str1)
        str2 = encode_to_base(str2)
        i=0
        res = []
        while(i<len(str1)):
            res.append(str1[i]^str2[i])
            i+=1
        res = bytes(res)
        return base_to_str(res)
st1='8f29336f5e9af0919634f474d248addaf89f6e1f533752f52de2dae0ec3185f818c0892fdc873a69'
st2='bf7962a3c4e6313b134229e31c0219767ff59b88584a303010ab83650a3b1763e5b314c2f1e2f166'


