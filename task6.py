import lab0_task2, lab0_task3

def repeated_key_xor(str_file):
    str = ''
    for line in str_file:
        str += line[: - 1]
    key_lenght = 2
    count = 0
    result_words_array = ['' for i in range(41)]
    #перевод из base64 в 16ю систему
    str = lab0_task2.base64_to_hex(str)
    print(str)

    while (key_lenght <= 40):
        words_array = ['' for i in range(key_lenght )]
        number_of_line = 0
        while(number_of_line < key_lenght):
            count = number_of_line*2
            while(count < len(str)):

                words_array[number_of_line] += str[count] + str[count + 1]
                count += key_lenght*2
            #расшифровываем строку по 1му символу (проверить на входные данные)

            words_array[number_of_line], s = lab0_task3.find_text(words_array[number_of_line])
            number_of_line +=1

        count_str = 0
        count_words_array = 0
        count_number_of_line = 0
        while(count_str < len(str)/2):
            count_words_array = count_str % key_lenght
            result_words_array[key_lenght] += words_array[count_words_array][count_number_of_line]
            if(count_words_array == key_lenght - 1):
                count_number_of_line += 1
            count_str += 1
        key_lenght += 1
    for x in result_words_array:
        print (x)

f = open('breakRepeatedKeyXor.txt', 'r')
repeated_key_xor(f)

f.close()