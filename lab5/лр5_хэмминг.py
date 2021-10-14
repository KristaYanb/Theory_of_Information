import sys

text = input("\nВведите текст (по-английски): ")
stroka = list(text.encode('utf-8'))
print("\nСимволы в ascii: ", stroka)

for i in (stroka):
    if (i >= 127) or (i <= 63) and (i >= 33) or (i <= 31):
        print("\nВведен русский текст или иные недопустимые символы!")
        sys.exit()

for i in range (len(stroka)):
    stroka[i] = bin(stroka[i])
    #print(stroka)
    stroka[i] = stroka[i][2:]
    if stroka[i] == '100000':
        stroka[i] = '0100000'
print("\nСимволы в бинарном виде: ", stroka)

#кодирование
for i in range(len(stroka)):
    stroka[i] = '00' + stroka[i]
    stroka[i] = stroka[i][:3] + '0' + stroka[i][3:]
    stroka[i] = stroka[i][:7] + '0' + stroka[i][7:]
print("\nДобавили нулевые контрольные биты: ", stroka)

for i in range(len(stroka)):                        #вычисляем контр биты
    if (int(stroka[i][0])+int(stroka[i][2])+int(stroka[i][4])+int(stroka[i][6])+int(stroka[i][8])+int(stroka[i][10])) % 2 == 1:
        stroka[i] = '0' + stroka[i][1:]
    else:
        stroka[i] = '1' + stroka[i][1:]
        
    if (int(stroka[i][1])+int(stroka[i][2])+int(stroka[i][5])+int(stroka[i][6])+int(stroka[i][9])+int(stroka[i][10])) % 2 == 1:
        stroka[i] = stroka[i][:1] + '0' + stroka[i][2:]
    else:
        stroka[i] = stroka[i][:1] + '1' + stroka[i][2:]

    if (int(stroka[i][3])+int(stroka[i][4])+int(stroka[i][5])+int(stroka[i][6])) % 2 == 1:
        stroka[i] = stroka[i][:3] + '0' + stroka[i][4:]
    else:
        stroka[i] = stroka[i][:3] + '1' + stroka[i][4:]

    if (int(stroka[i][7])+int(stroka[i][8])+int(stroka[i][9])+int(stroka[i][10])) % 2 == 1:
        stroka[i] = stroka[i][:7] + '0' + stroka[i][8:]
    else:
        stroka[i] = stroka[i][:7] + '1' + stroka[i][8:]
print("\nЗакодированная строка с вычисленными контрольными битами: ", stroka)     #закодированная строка

for i in range(len(stroka)):
    print (stroka[i],end=' ')
print('\n')

for i in range(len(stroka)):
    print (stroka[i],end='')
print('\n')
    
str_decode = input("\nВведите строку (искаженную): ")

for i in range(len(str_decode)):
    if (str_decode[i] != '0') and (str_decode[i] != '1'):
        print("\nНеправильно введены данные!")
        sys.exit()
if len(str_decode) != len(stroka)*11:
    print("\nНеправильная длина сообщения!")
    sys.exit()

msg_str_decode = []                                 #делим получ строку на подстроки
while str_decode != '':
    msg_str_decode.append(str_decode[:11])
    str_decode = str_decode[11:]
print("\nРазделенное сообщение: ", msg_str_decode)

count=[]
for i in range(len(stroka)):
    count.append(0)
    #count = 0
    for j in range(len(stroka[i])):
        if (stroka[i][j] != msg_str_decode[i][j]) and (j!=0) and (j!=1) and (j!=3) and (j!=7):
            #count = count + 1
            count[i] = count[i] + 1
            print("Место ошибки в {}-м символе - {}".format(i+1, j+1))

for i in range(len(count)):
    if count[i] > 1:
        print("\nКол-во ошибок больше одной!")
        sys.exit()
    
for i in range(len(msg_str_decode)):                #вычисляем контр биты 
    if (int(msg_str_decode[i][2])+int(msg_str_decode[i][4])+int(msg_str_decode[i][6])+int(msg_str_decode[i][8])+int(msg_str_decode[i][10])) % 2 == 1:
        msg_str_decode[i] = '0' + msg_str_decode[i][1:]
    else:
        msg_str_decode[i] = '1' + msg_str_decode[i][1:]
        
    if (int(msg_str_decode[i][2])+int(msg_str_decode[i][5])+int(msg_str_decode[i][6])+int(msg_str_decode[i][9])+int(msg_str_decode[i][10])) % 2 == 1:
        msg_str_decode[i] = msg_str_decode[i][:1] + '0' + msg_str_decode[i][2:]
    else:
        msg_str_decode[i] = msg_str_decode[i][:1] + '1' + msg_str_decode[i][2:]

    if (int(msg_str_decode[i][4])+int(msg_str_decode[i][5])+int(msg_str_decode[i][6])) % 2 == 1:
        msg_str_decode[i] = msg_str_decode[i][:3] + '0' + msg_str_decode[i][4:]
    else:
        msg_str_decode[i] = msg_str_decode[i][:3] + '1' + msg_str_decode[i][4:]

    if (int(msg_str_decode[i][8])+int(msg_str_decode[i][9])+int(msg_str_decode[i][10])) % 2 == 1:
        msg_str_decode[i] = msg_str_decode[i][:7] + '0' + msg_str_decode[i][8:]
    else:
        msg_str_decode[i] = msg_str_decode[i][:7] + '1' + msg_str_decode[i][8:]
print("\nИскаженное сообщение с заново вычисленными контрольными битами: ", msg_str_decode) 

mesto = []                                          #места ошибок в контр битах
for i in range(len(stroka)):
    mesto_osh = 0
    if (stroka[i] != msg_str_decode[i]):
        for j in range(len(stroka[i])):
            if (stroka[i][j] != msg_str_decode[i][j]) and ((j==0) or (j==1) or (j==3) or (j==7)):
                    mesto_osh = mesto_osh + (j + 1)
    mesto.append(mesto_osh)
print("\nМеста ошибок в словах: ", mesto)

for i in range(len(msg_str_decode)):                #инвертируем место ошибки
    if mesto[i] == 0:
        i = i + 1
    else:
        if int(msg_str_decode[i][(mesto[i]-1)]) == 0:
            msg_str_decode[i] = msg_str_decode[i][:(mesto[i]-1)] + '1' + msg_str_decode[i][(mesto[i]):]
        else:
            msg_str_decode[i] = msg_str_decode[i][:(mesto[i]-1)] + '0' + msg_str_decode[i][(mesto[i]):]
print("\nСообщение с инвертированными ошибками: ", msg_str_decode)

decode = ''                                         #убираем контр биты
for i in range(len(msg_str_decode)):
    msg_str_decode[i] = msg_str_decode[i][2] + msg_str_decode[i][4:7] + msg_str_decode[i][8:]
    msg_str_decode[i] = chr(int(msg_str_decode[i], base = 2))
    decode = decode + msg_str_decode[i]
print("\nДекодированное сообщение: ", decode)

