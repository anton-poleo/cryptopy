
arr_base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
def hex_to_bin(str):
    if(len(str)!=6):
        return None
    dec_str = 0
    for j in range(3):
        char_code = int(str[j * 2:j * 2 + 2:], 16)
        dec_str += (char_code << (2 - j) * 8)
    #bin_str = '0' * (24 - len(bin(dec_str)[2:])) + bin(dec_str)[2:]
    bin_str = '{0:0>24}'.format(bin(dec_str)[2:])
    return bin_str

def bin_to_base(bin_str, amount_zero):
    if len(bin_str) != 24:
        return  None
    str_base64 = ''
    #количество ненулевых битовых строк в 24 символах
    amount_units = int(4 - amount_zero)
    for i in range(amount_units):
        position = int(bin_str[6 * i: 6 * i + 6:], 2)
        str_base64 += arr_base64[position]
    return str_base64
def hex_to_base64(str):
    if (len(str)%2 != 0) and (len(str) != 0):
        return None
    res = ''
    #количество блоков длины 6
    amount_unit = int((len(str) / 2) // 3)
    #количество необработанных байт
    amount_zero = int((len(str) / 2) % 3)
    for i in range(amount_unit):
        bin_str = hex_to_bin(str[i * 6: i * 6 + 6:])
        res += bin_to_base(bin_str, 0)
    if (amount_zero == 2):
        bin_str = hex_to_bin(str[(amount_unit - 1) * 6 + 6:] + '0' * 2)
        res += bin_to_base(bin_str, 1) + '='
    if (amount_zero == 1):
        bin_str = hex_to_bin(str[(amount_unit - 1) * 6 + 6:] + '0' * 4)
        res += bin_to_base(bin_str, 2) + '=='
    return res
str = 'faea8766efd8b295a633908a3c0828b22640e1e9122c3c9cfb7b59b7cf3c9d448bf04d72cde3aaa0'

#print(hex_to_base64(str))
#print('+uqHZu/YspWmM5CKPAgosiZA4ekSLDyc+3tZt888nUSL8E1yzeOqoA==')


#______________________________________________________________________------------------------_____________________________



arr_base64_2=['A000000', 'B000001', 'C000010', 'D000011', 'E000100', 'F000101', 'G000110', 'H000111', 'I001000', 'J001001', 'K001010', 'L001011', 'M001100', 'N001101', 'O001110', 'P001111', 'Q010000', 'R010001', 'S010010', 'T010011', 'U010100', 'V010101', 'W010110', 'X010111', 'Y011000', 'Z011001', 'a011010', 'b011011', 'c011100', 'd011101', 'e011110', 'f011111', 'g100000', 'h100001', 'i100010', 'j100011', 'k100100', 'l100101', 'm100110', 'n100111', 'o101000', 'p101001', 'q101010', 'r101011', 's101100', 't101101', 'u101110', 'v101111', 'w110000', 'x110001', 'y110010', 'z110011', '0110100', '1110101', '2110110', '3110111', '4111000', '5111001', '6111010', '7111011', '8111100', '9111101', '+111110', '/111111']

def base64_to_bin(str_base):
    if(len(str_base) != 4):
        return None
    bin_str = ''
    #создаем словарь {символ : ее двоичное значение в base64}
    dict_base64 = {}
    for x in arr_base64_2:
        dict_base64[x[:1]] = x[1:]
    for i in range(4):
        if(str_base[i] != '='):
            bin_str += dict_base64[str_base[i]]
        else:
            bin_str += '000000'
    return bin_str

def bin_to_hex(str_bin, amount_zero):
    if (len(str_bin) != 24):
        return None
    str = ''
    amount_unit = int(3 - amount_zero)
    for i in range(amount_unit):
        hex_str_byte = hex(int(str_bin[8 * i:8 * i + 8:], 2))[2:]
        hex_str_byte = '{0:0>2}'.format(hex_str_byte)
        str += hex_str_byte
    return str

#print(bin_to_hex('010111010001010100010001', 0))

def base64_to_hex(str_base):
    if(len(str_base)%4 != 0) and (len(str_base) != 0):
        return None
    #количество 4хзначных блоков в str_base
    amount_unit = int(len(str_base)/4)
    res = ''
    for x in range(amount_unit - 1):
        bin_str = base64_to_bin(str_base[x * 4:x * 4 + 4:])
        res += bin_to_hex(bin_str, 0)
    if (str_base[(amount_unit-1)*4 + 3]) != '=':
        bin_str = base64_to_bin(str_base[(amount_unit - 1) * 4:(amount_unit - 1) * 4 + 4:])
        res += bin_to_hex(bin_str, 0)
    elif ((str_base[(amount_unit-1)*4 + 3]) == '=') and ((str_base[(amount_unit-1)*4 + 2]) != '='):
        bin_str = base64_to_bin(str_base[(amount_unit - 1) * 4:(amount_unit - 1) * 4 + 4:])
        res += bin_to_hex(bin_str, 1)
    else:
        bin_str = base64_to_bin(str_base[(amount_unit - 1) * 4:(amount_unit - 1) * 4 + 4:])
        res += bin_to_hex(bin_str, 2)
    return res
#print(base64_to_hex('+uqHZu/YspWmM5CKPAgosiZA4ekSLDyc+3tZt888nUSL8E1yzeOqoA=='))
print(base64_to_hex('+uqHZu/YspWmM5CKPAgosiZA4ekSLDyc+3tZt888nUSL8E1yzeOqoA=='))
prt = 'faea8766efd8b295a633908a3c0828b22640e1e9122c3c9cfb7b59b7cf3c9d448bf04d72cde3aaa0'
print(prt)