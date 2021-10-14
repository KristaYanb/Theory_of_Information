import sys

def compress(stroka):               
    dictionary = {}                 #словарь (символ и его номер) нум с 1
    p = ""                          #то, что повторилось (было в словаре)
    code = []                      
    i = 0                           
    
    while i < len(stroka):
        char = stroka[i]            
        try:                        #проверка наличия в словаре
            dictionary[p + char]    #есть в словаре? нет -> except
            p = p + char            #да -> след символ
        except:
            if p == "":             #до текущего симв символ не был, то 
                o = 0               #в скобках число = 0
            else:
                o = dictionary[p]       #был, то смещение до первого появления предыд симв в строке
            code.append((o, char))      #добавили в код пару (смещение-тек символ)
            dictionary[p + char] = len(dictionary) + 1   #увеличили для символа его номер
            p = ""                      #заново
            
        i += 1                         

        if (p != "") and (i >= len(stroka)):    #остаточная часть (посл симв)
            code.append((dictionary[p], ''))    #если он был в словаре
            break
    print(dictionary)
    return code


def decompress(code):                   
    dictionary = []                     #словарь(как список-нум с 0)
    p = ""
    
    for (w, char) in code:              #по парам кода (смещение-тек символ)
        if w == 0:                      #если не было симв до этого
            p = ""                      #то просто тек симв в словарь
        else:                           #был
            p = dictionary[w-1]         #то плюс с симв под ном w в словарь
        dictionary.append(p + char)     #добавляем в словарь

    stroka_new = ""                     
    for symb in dictionary:            
        stroka_new += symb
        
    return stroka_new


stroka = input("\nВведите текст для сжатия: ")
if len(stroka) == 0:
    sys.exit()
    
a = compress(stroka)
print ("\nРезультат сжатия: ", a)

b = decompress(a)
print ("\nРезультат распаковки: ", b)
