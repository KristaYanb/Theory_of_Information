import fractions as fr
import sys

def coding_decoding(freq, text):
#кодирование
        interspace = {}         #симв - промежуток
        low = fr.Fraction(0, 1)
        for item in freq:
                high = fr.Fraction(freq[item], n)
                interspace[item] = [low, low+high]
                low = low+high
        #print(interspace)

        print("\nТаблица промежутков: ")
        for item in interspace:
                print(item, end=" ")
                print(interspace[item][0], end=" ")
                print(interspace[item][1])

        oldLow = fr.Fraction(0, 1)
        oldHigh = fr.Fraction(1, 1)

        for char in text:
                newLow = oldLow + (oldHigh - oldLow) * interspace[char][0]
                newHigh = oldLow + (oldHigh - oldLow) * interspace[char][1]
                oldLow = newLow
                oldHigh = newHigh

        print("\nНижняя граница промежутка - результат кодирования: {} = {}".format(oldLow, float(oldLow)))
        #print("\nНижняя граница промежутка - результат кодирования: ", oldLow)
        #print("\nВерхняя граница промежутка: ", oldHigh)
        #print ("Код в другом виде: ", str(float(oldLow)).split('.')[1])
        print("\nВерхняя граница промежутка: {} = {}".format(oldHigh, float(oldHigh)))
        print ("\nРезультат кодирования: ", (oldLow+oldHigh)/2)
        
#декодирование
        decode = ""
        code = (oldLow+oldHigh)/2
        #code = oldLow
        for i in range(n):
                for item in interspace:
                        if code >= interspace[item][0] and code < interspace[item][1]:
                                #print(interspace[item][0])
                                decode += item
                                code = (code-interspace[item][0])/(interspace[item][1]-interspace[item][0])
                                #print(code)
                                break
        print ("\nРезультат декодирования: ", decode)

text = input("\nВведите сообщение: ")
n = len(text)
if n == 0:
        sys.exit(0)
print("\nДлина сообщения: ", n)

freq = {}               #симв-част
for i in range(n):
        if text[i] in freq:
                freq[text[i]] += 1
        else:
                freq[text[i]] = 1
#print(freq)
                
print("\nЧастоты и вероятности:")
for char in freq:
        print("\nСимвол: {}, частота: {}, вер-ть: {}".format(char, freq[char], freq[char]/len(text)))

coding_decoding(freq, text)
