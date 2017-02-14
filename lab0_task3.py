from lab0_task1 import xor
import math
import re
import binascii
import base64
from base64 import b64encode, b64decode
str = '041811045013111e5003110615501815025000151f001c1550111e1450021503041f0215'

a=65
#print(chr(a))
frequency = [ 8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074 ]

#Берем только бувы и переводим их в нижнй регистр
def find_letters(str):
    res = ''
    for x in str:
        y = ord(x)
        if((y > 64) and (y < 91)):
            res += chr(y+32)
        elif((y > 96)and(y<123)):
            res += x
    return res

#Ищем частоту английских букв
def find_freq(str):
    res = [0 for i in range(26)]
    freq = 0#дельта частоты
    i = 0

    str = find_letters(str)
    if (len(str) == 0):
        return 1000
    for x in str:
        y = ord(x)
        #print(y)
        res[y-97]+=1
    while(i < 26):
        freq += math.fabs(frequency[i]/100 - res[i]/len(str))
        i+=1
    return freq

def find_text(str):
    dec_value = 0
    #print(str)
    m1 = 1000
    while(dec_value<=255):
        #print(dec_value)


        ptr = '{0:0>2}'.format(hex(dec_value)[2:])
        i = 0
        while (i<(len(str)/2) - 1):


            ptr += '{0:0>2}'.format(hex(dec_value)[2:])
            i+=1
        dec_value+=1
        if(len(str)!=len(ptr)):
            print(str)
            print(ptr)
        #if(len(str) == 0):
        #    ptr = ''
        res = xor(str, ptr)
        #print(res)
        v = ''
        j = 2
        z = 0
        while (j < len(res) + 2):
            k = int(res[z:j], 16)
            v += chr(k)
            j += 2
            z += 2

        value_of_freq1 = find_freq(v)
        if (value_of_freq1 <= m1):
            m1 = value_of_freq1
            final_value1 = v
              #print(final_value1)
        #print(find_letters(v))
        #print(v)

    return final_value1, m1

