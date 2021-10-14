import sys

def groups(symbol_freq_code):                             #ф-ия разбивания на две группы по частотам
    all_freq = sum(elem[1] for elem in symbol_freq_code)  #общая частота группы

    count = 0                                    #кол-во эл-тов в первой (левой) группе 
    part_freq = 0                                #частота подгруппы 
    min_razn = all_freq                          #мин разность частот для учета разбиения на группы

    for elem in symbol_freq_code:                #определяем группы 
        part_freq += elem[1]                     # + очередная частота
        razn = abs(all_freq - 2 * part_freq)     #проверка разницы м/у всей частотой гр и удвоенной частотой подгр (тк 2 гр)
        
        if min_razn > razn:                      #если мин разн > вычисленной
            min_razn = razn                      #меняем мин разн
        else:                                    #иначе завершаем деление на группы
            break

        count += 1
        
    return symbol_freq_code[:count], symbol_freq_code[count:]   #имеем две группы по частотам (левая и правая)


def coding(symbol_freq_code):                   #ф-ия кодирования
    if len(symbol_freq_code) == 1:              #если длина очередного списка = 1, то прекращаем его кодировать
        return

    first, second = groups(symbol_freq_code)    #делим на две группы ф-ей разбивания

    for elem in first:                          #для левой - ноль
        elem[2] += '0'                          #в код

    for elem in second:                         #для правой - единицу
        elem[2] += '1'                          #в код

    coding(first)                               #рекурсивно кодируем левую группу
    coding(second)                              #рекурсивно кодируем правую группу

stroka = input("\nВведите текст для шифрования: ")
if len(stroka) == 0:
    sys.exit()
    
flag = 0 
symbol_freq = []                            #список пар (символ - частота)
count_for = 0

for i in range(len(stroka)):                #поиск частот каждого символа и в список
    for j in range(len(symbol_freq)):
        if stroka[i] == symbol_freq[j][0]:
            symbol_freq[j][1] += 1
            flag = 1
    if flag == 0:
        symbol_freq.append([stroka[i], 1])   #добавляем элемент [символ - частота] в конец списка
        count_for += 1
    flag = 0

print(symbol_freq)                           #выведем список пар (символ - частота)

encoded_one = ''
if count_for == 1:
    for i in range(len(stroka)):
        encoded_one += '0'
    print ("Закодированный текст: ", encoded_one)
    print("Кол-во различных символов: {}, длина кода: {}".format(len(symbol_freq), len(encoded_one)))
    sys.exit()
    
symbol_freq_code = []                        #новый список троек (символ - частота - код)
for i in range(len(symbol_freq)):
    symbol_freq_code.append(([str(symbol_freq[i][0]), symbol_freq[i][1], '']))

symbol_freq_code = sorted(symbol_freq_code, key = lambda freq: freq[1], reverse = True)   #сортируем по убыванию частоты
coding(symbol_freq_code)                     #кодируем

for elem in sorted(symbol_freq_code):        #по алфавиту       
    print("{}: {}".format(elem[0], elem[2])) #выводим пару (символ - код)

encoded = ''                                 #выведем закодированную строку
for i in range(len(stroka)):
    for elem in symbol_freq_code:
        if stroka[i] == elem[0]:
            encoded += elem[2]
            encoded += ' '
print("Закодированный текст: ", encoded)

a = ''
list_encoded = encoded.split()
print(list_encoded)
for i in range(len(list_encoded)):
    for elem in symbol_freq_code:
        if list_encoded[i] == elem[2]:
            a += elem[0]    

print("Кол-во различных символов: {}, длина кода: {}".format(len(symbol_freq), len(encoded)))
print("Декодированный текст: ", a)
