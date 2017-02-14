import lab0_task1
import lab0_task3
def detection_xor(file_str):

    res_dict = {}
    for line in file_str:
        #print(line)
        str, freq = lab0_task3.find_text(line[:len(line) - 3])
        res_dict[freq] = str
    #print(sorted(res_dict.keys()))
    x = sorted(res_dict.keys())
    #print(res_dict.values())
    return res_dict[x[0]]

#file_str = open('detectSingleXor14', 'r')
#print(detection_xor(file_str))
#file_str.close()
