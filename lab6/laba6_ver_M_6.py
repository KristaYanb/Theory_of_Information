import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import copy, sys

indexes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '$', '%', '*', '+', '-', '.', '/', ':']

polynom = [251, 67, 46, 61, 118, 70, 64, 94, 32, 45] #генерир мн-н

galois = [ 1, 2, 4, 8, 16, 32, 64, 128, 29, 58, 116, 232, 205, 135, 19, 38,                   #поле Галуа
                            76, 152, 45, 90, 180, 117, 234, 201, 143, 3, 6, 12, 24, 48, 96, 192,
                            157, 39, 78, 156, 37, 74, 148, 53, 106, 212, 181, 119, 238, 193, 159, 35,
                            70, 140, 5, 10, 20, 40, 80, 160, 93, 186, 105, 210, 185, 111, 222, 161,
                            95, 190, 97, 194, 153, 47, 94, 188, 101, 202, 137, 15, 30, 60, 120, 240,
                            253, 231, 211, 187, 107, 214, 177, 127, 254, 225, 223, 163, 91, 182, 113, 226,
                            217, 175, 67, 134, 17, 34, 68, 136, 13, 26, 52, 104, 208, 189, 103, 206,
                            129, 31, 62, 124, 248, 237, 199, 147, 59, 118, 236, 197, 151, 51, 102, 204,
                            133, 23, 46, 92, 184, 109, 218, 169, 79, 158, 33, 66, 132, 21, 42, 84,
                            168, 77, 154, 41, 82, 164, 85, 170, 73, 146, 57, 114, 228, 213, 183, 115,
                            230, 209, 191, 99, 198, 145, 63, 126, 252, 229, 215, 179, 123, 246, 241, 255,
                            227, 219, 171, 75, 150, 49, 98, 196, 149, 55, 110, 220, 165, 87, 174, 65,
                            130, 25, 50, 100, 200, 141, 7, 14, 28, 56, 112, 224, 221, 167, 83, 166,
                            81, 162, 89, 178, 121, 242, 249, 239, 195, 155, 43, 86, 172, 69, 138, 9,
                            18, 36, 72, 144, 61, 122, 244, 245, 247, 243, 251, 235, 203, 139, 11, 22,
                            44, 88, 176, 125, 250, 233, 207, 131, 27, 54, 108, 216, 173, 71, 142, 1]

obr_galois = [ -1, 0, 1, 25, 2, 50, 26, 198, 3, 223, 51, 238, 27, 104, 199, 75,                 #обр поле Галуа
                     4, 100, 224, 14, 52, 141, 239, 129, 28, 193, 105, 248, 200, 8, 76, 113,
                     5, 138, 101, 47, 225, 36, 15, 33, 53, 147, 142, 218, 240, 18, 130, 69,
                     29, 181, 194, 125, 106, 39, 249, 185, 201, 154, 9, 120, 77, 228, 114, 166,
                     6, 191, 139, 98, 102, 221, 48, 253, 226, 152, 37, 179, 16, 145, 34, 136,
                     54, 208, 148, 206, 143, 150, 219, 189, 241, 210, 19, 92, 131, 56, 70, 64,
                     30, 66, 182, 163, 195, 72, 126, 110, 107, 58, 40, 84, 250, 133, 186, 61,
                     202, 94, 155, 159, 10, 21, 121, 43, 78, 212, 229, 172, 115, 243, 167, 87,
                     7, 112, 192, 247, 140, 128, 99, 13, 103, 74, 222, 237, 49, 197, 254, 24,
                     227, 165, 153, 119, 38, 184, 180, 124, 17, 68, 146, 217, 35, 32, 137, 46,
                     55, 63, 209, 91, 149, 188, 207, 205, 144, 135, 151, 178, 220, 252, 190, 97,
                     242, 86, 211, 171, 20, 42, 93, 158, 132, 60, 57, 83, 71, 109, 65, 162,
                     31, 45, 67, 216, 183, 123, 164, 118, 196, 23, 73, 236, 127, 12, 111, 246,
                     108, 161, 59, 82, 41, 157, 85, 170, 251, 96, 134, 177, 187, 204, 62, 90,
                     203, 89, 95, 176, 156, 169, 160, 81, 11, 245, 22, 235, 122, 117, 44, 215,
                     79, 174, 213, 233, 230, 231, 173, 232, 116, 214, 244, 234, 168, 80, 88, 175 ]

searching_elements = [      #поисков узоры
    [1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,1,0,1],
    [1,0,1,0,0,0,1,0,1],
    [1,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1]]

def coding(inputs):     #на 2 симв 11 бит инф
    i = 0
    split_str = ""
    for i in range(i, len(inputs), 2):
        split_by_two = inputs[i:i+2:1]
        if len(split_by_two) == 2:
            temp_dec = 45 * indexes.index(split_by_two[0]) + indexes.index(split_by_two[1])
            temp = bin(temp_dec)[2:]
            split_str += temp.rjust(11, '0')    #дополняем до 11 бит
            
        if len(split_by_two) == 1:
            temp = bin(indexes.index(split_by_two))[2:]  
            split_str += temp.rjust(6, '0')     #дополняем до 6 бит
            
    #добавл служ инф - спос кодиров и кол-во данных
    count_str = (bin(len(inputs))[2:]).rjust(9, '0') #дополняем до 9 бит
    return "0010" + count_str + split_str

def fill(for_fill): #заполн до длины для версии, чтобы дл последоват была кратна 8
    max_inf = 128   #макс кол-во инф (со служебн) в битах, к-рое можно закодир в этой версии
    add1 = "11101100"
    add2 = "00010001"
    
    for i in range(0,4):        #добавл нули (макс 4) до кратности
        if len(for_fill) != max_inf:
            for_fill += '0'
        else:
            return for_fill

    while len(for_fill) % 8 != 0:
        for_fill += '0'
        
    i = 0                       #чередуем байты
    while len(for_fill) != max_inf:
        if i % 2 == 0:
            for_fill += add1
            i += 1
            continue
        for_fill += add2
        i += 1
    return for_fill

def forming_blocks(data): 
    count_of_bytes = len(data)//8   #дел инф на блоки по 8 бит
    bytes_as_decimals = []          #перев в 10 СС
    for k in range(0, len(data), 8):
        bytes_as_decimals.append(int(data[k:k+8:1], 2))

    blocks = []
    blocks.append(bytes_as_decimals[0: count_of_bytes: 1])
    return blocks

def correcting_bytes(blocks_):              #созд кол-во байт в зав-ти от ур коррекц
    #заполн массив данными из блока и нулями
    count_of_correcting = 10                #кол-во байтов коррекц
    for i in range(0, len(blocks_)):        #для кажд блока данных
        len_blocks = len(blocks_[i])
        while len(blocks_[i]) < count_of_correcting: #если блок данных < коррект, то добавл 0
            blocks_[i].append(0)
        for j in range(0, len_blocks):      #до прибавл нулей уже засекли кол-во байт в len_blocks
            temp_A = blocks_[i][0]
            blocks_[i].pop(0)
            blocks_[i].append(0)
            if temp_A == 0:
                continue
            temp_B = obr_galois[temp_A]
            place = 0
            for k in polynom:
                temp_D = (temp_B + k) % 255
                temp_D = galois[temp_D]
                blocks_[i][place] ^= temp_D #xor эл-тов одного индекса с полиномом и массивом данных
                place += 1
    for k in range(len(blocks_)):           #если байт данных > размера коррект => обрезаем нули с конца в коррект блоке
        while len(blocks_[k]) > count_of_correcting:
            blocks_[k].pop()
    return blocks_

def merge_blocks(blocks, blocks_of_correct):        #объед блоков (данные + байты коррекц)
    merged = []
    
    flag = True     #добавл данных
    while flag:
        for i in range(len(blocks)):
            if len(blocks[i]) == 0:
                flag = False
                break
            if len(blocks[i]) != 0:
                merged.append(blocks[i].pop(0))
                
    flag = True     #добавл коррект
    while flag:     
        for i in range(len(blocks_of_correct)):
            if len(blocks_of_correct[len(blocks_of_correct) - 1]) == 0:
                flag = False
                break
            if len(blocks_of_correct[i]) != 0:
                merged.append(blocks_of_correct[i].pop(0))
    return merged

def draw_searching(pixels):         #рис поиск узоры (3 шт)
    for i in range(len(searching_elements)-1):
        for j in range(len(searching_elements)-1):
            pixels[i][j] = searching_elements[i+1][j+1]                  #лев верхн
            pixels[i][len(pixels) - 8 + j] = searching_elements[i+1][j]  #лев нижн
            pixels[len(pixels) - 8 + i][j] = searching_elements[i][j+1]  #прав верхн
    return pixels

def draw_synchronization(pixels):   #полосы синхр (черн-бел)
    i = 8
    for i in range(i, len(pixels)-8):
        if i % 2 != 0:
            pixels[6][i] = 1
            pixels[i][6] = 1
            continue
        pixels[6][i] = 0
        pixels[i][6] = 0
    return pixels

def draw_mask_correct(pixels):      #код маски и ур коррекц
    code = "101010000010010"        #нулев маска и ур корекц М(15%)
    #заполн вокруг лев верхн 
    place = 0               #0-7 биты
    for j in range(0,8):
        if pixels[8][j] == -1:
            pixels[8][j] = int(code[place])^1
            place += 1
    i = 8                   #8-14 биты
    while i >= 0:
        if pixels[i][8] == -1:
            pixels[i][8] = int(code[place])^1
            place += 1
        i -= 1
    #заполн рядом с нижн лев и верхн прав
    place = 0               #0-7 биты     
    j = len(pixels) - 1
    while j > len(pixels) - 8:
        if pixels[j][8] == -1:
            pixels[j][8] = int(code[place])^1
            place += 1
        j -= 1
        
    pixels[len(pixels)-8][8] = 0 #ставим черн статичный модуль
    j = len(pixels)-8       #8-14 биты
    while j < len(pixels):
        if pixels[8][j] == -1:
            pixels[8][j] = int(code[place])^1
            place += 1
        j += 1

    return pixels

def is_mask_true(row,col):      #маска = 1 => не инвертир бит
    return (row+col)%2 == 1 

def draw_data(pixels, data):    #добавл данных
    size = len(pixels)
    str_bits = ""
    for k in data:
        str_bits += (bin(k)[2:]).rjust(8, '0') #дополняем до 8 бит

    i = size - 1
    j = size - 1
    place = 0
    try:
        up_forw_module = True
        while j > 0:                            #идём по столбцам справа налево и отнимаем 2 - один модуль
            if up_forw_module:
                for i in range(size - 1, -1, -1):
                    if pixels[i][j] == -1:      #пр
                        pixels[i][j] = (int(str_bits[place]) ^ 1) if is_mask_true(i,j) else int(str_bits[place])
                        place += 1
                    if pixels[i][j-1] == -1:    #лев
                        pixels[i][j-1] = (int(str_bits[place]) ^ 1) if is_mask_true(i,j-1) else int(str_bits[place])
                        place += 1
                up_forw_module = False          #след модуль вниз
            else:
                for i in range(0, size, 1):
                    if pixels[i][j] == -1:      #пр
                        pixels[i][j] = (int(str_bits[place])^1) if is_mask_true(i,j) else int(str_bits[place])
                        place += 1
                    if pixels[i][j-1] == -1:    #лев
                        pixels[i][j-1] = (int(str_bits[place])^1) if is_mask_true(i,j-1) else int(str_bits[place])
                        place += 1
                up_forw_module = True           #след модуль вверх 
            j -= 2
            if j == 6:                          #лев полоса синхр
                j -= 1
        return pixels
    except IndexError as e:                     #т.к. кол-ва бит данных мб < своб места
        return pixels
    return pixels

print("Можно закодировать макс 20 символов из: латинского алфавита, цифр, символов $%*+-./: и пробела")

inputs = input("Введите текст для кодирования: ")
inputs = inputs.upper()
for i in inputs:
    if i not in indexes:
        print("В тексте присутствуют недопустимые символы!")
        sys.exit()
        
for_fill = coding(inputs)
if len(for_fill) > 128:
    print("\nКол-во символов в тексте > 20!")
    sys.exit()
    
to_form_blocks = fill(for_fill)
print(to_form_blocks)
print(len(to_form_blocks))
blocks = forming_blocks(to_form_blocks)
blocks_of_correct = copy.deepcopy(blocks)
correcting_bytes(blocks_of_correct)
data = merge_blocks(blocks, blocks_of_correct)
"""res = ""
for i in to_form_blocks:
    res += bin(i)[2:]
print(res)
print(len(res))"""

img = Image.new('1', (21+8, 21+8), color = 'white')
pixels = np.full((21,21),-1)
img_pixels = img.load()

draw_searching(pixels)
draw_synchronization(pixels)
draw_mask_correct(pixels)
draw_data(pixels, data)

for i in range(img.size[0]-8):      #nd.array в пиксели
    for j in range(img.size[0]-8):
        if (pixels[i][j] != -1):
            img_pixels[j+4, i+4] = int(pixels[i][j])

plt.imshow(np.asarray(img), cmap = 'gray')
plt.axis('off')
plt.show()
