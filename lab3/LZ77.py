import sys

def find_in_dict(buffer, dictionary):          
    
    shift = len(dictionary)                    
    substring = ""                              

    for char in buffer:                         #для каждого симв буфера
        substring_tmp = substring + char        #временная подстрока (добавл симв буфера к подстроке)
        shift_tmp = dictionary.rfind(substring_tmp) #номер подстроки в словаре

        if shift_tmp < 0:                       
            break
                                            
        substring = substring_tmp               #полученная подстрока
        shift = shift_tmp                       #номер подстроки, найд до этого(до выхода) в словаре

    return len(substring), len(dictionary) - shift      #дл найд эл-та словаря и дл словаря без номера подстроки в нем(смещение)


def compress(message, buffer_size, dictionary_size):   
    
    dictionary = ""                                     
    buffer = message[:buffer_size]                      
    output = []                                         
    
    while len(buffer) != 0:                            
        size, shift = find_in_dict(buffer, dictionary)  #берем размер подстроки и словаря без номера подстроки в нем

        dictionary += message[:size + 1]                #добавл в словарь то, что в буфере до размера подстроки и + еще симв
        dictionary = dictionary[-dictionary_size:]      #если размер словаря превышен => оставляем по его размеру с конца
        #print(dictionary)
        message = message[size:]                        #убираем найденную строку из сообщения
        last_char = message[:1]                         #первый симв после найденной строки
        message = message[1:]                           #ост сообщение после первого симв

        buffer = message[:buffer_size]                  #в буфер след сообщ до размера буфера
        output.append((shift, size, last_char))         
        
    return output


def decompress(code):                       
    stroka_new = ""                         
    for (shift, size, char) in code:   #для каждой тройки кода
        stroka_new = stroka_new + stroka_new[-shift:][:size] + char    #добавл после размера очереди с конца и до размера + сам эл-т
    return stroka_new

stroka = input("\nВведите текст для сжатия: ")
if len(stroka) == 0:
    sys.exit()

buffer_size = 0
dictionary_size = 0

buffer_size = int(input("\nВведите размер буфера: "))
dictionary_size = int(input("\nВведите размер словаря: "))

a = compress(stroka, buffer_size, dictionary_size)
print("\nРезультат сжатия: ", a)

b = decompress(a)
print("\nРезультат распаковки: ", b)
