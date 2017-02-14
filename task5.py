import lab0_task1
import binascii
str = 'Never trouble about trouble until trouble troubles you!'
#str_key = 'ICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEICEI'
key_word = 'ICE'

num_word = len(str)//len(key_word)
num_letter = len(str)%len(key_word)
str_key = key_word*num_word + key_word[:num_letter]
print(str_key)



def repeat_detect(str, str_key):
    ptr = binascii.b2a_hex(str.encode()).decode()
    ptr_key = binascii.b2a_hex(str_key.encode()).decode()
    return lab0_task1.xor(ptr, ptr_key)
print(repeat_detect(str, str_key))