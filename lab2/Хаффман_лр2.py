import heapq, sys                              #модуль для создания списка - очереди с приоритетами
from collections import Counter, namedtuple    #класс для подсчета отд эл-тов и ф-ция для созд своего типа кортежа

#структура дерева: листья и узлы
class Leaf_of_tree(namedtuple("Leaf_of_tree", ["char"])):  #класс для листьев дерева; у него нет потомков, но есть значение символа
    def walk(self, code, tree):                 #обход дерева
        code[self.char] = tree or "0"           #либо ноль, либо прошлый путь; запись кода символа

class Unit_of_tree(namedtuple("Unit_of_tree", ["left", "right"])):  #класс для ветвей дерева - внутренних узлов; у них есть потомки
    def walk(self, code, tree):                 #обход дерева
        self.left.walk(code, tree + "0")        #левый потомок
        self.right.walk(code, tree + "1")       #правый потомок

def huffman_encode(stroka):                     #ф-ция кодирования
    heap = []                                   #создали список
    for symbol, frequency in Counter(stroka).items():               #цикл для списка с помощью счетчиков символов
        heap.append((frequency, len(heap), Leaf_of_tree(symbol)))   #добавляем в список: частота, счетчик, символ - лист
    heapq.heapify(heap)                         #упорядочиваем элементы списка -> очередь с приоритетами
    count_of_symbols = len(heap)                #кол-во симв в списке - для счетчика
    
    while len(heap) > 1:                        #пока хотя бы два эл-та в очереди
        frequency1, count1, left = heapq.heappop(heap)      #берем узел левый с мин частотой
        frequency2, count2, right = heapq.heappop(heap)     #берем узел правый с частотой после мин
        heapq.heappush(heap, (frequency1 + frequency2, count_of_symbols, Unit_of_tree(left, right))) #новый узел, у к-рого потомки выше
        count_of_symbols += 1                   #увелич счетчик при добавлении нового эл-та для их идентификации

    code = {}                                   #словарь кодов символов
    [(frequency3, count3, root)] = heap         #после цикла один эл-т - корень дерева
    root.walk(code, "")                         #обход дерева с корня
    return code

stroka = input("\nВведите текст для шифрования: ")
if len(stroka) == 0:
    sys.exit()
    
symbol_freq = [(symbol_, _freq) for symbol_, _freq in Counter(stroka).items()]  #частоты символов
print(symbol_freq)

code = huffman_encode(stroka)                           #кодируем

for symbol in sorted(code):                             #по алфавиту
    print("{}: {}".format(symbol, code[symbol]))        #выводим пару (символ - код)

encoded = "".join(code[symbol] for symbol in stroka)    #выведем закодированную строку
print("Закодированный текст: ", encoded)

print("Кол-во различных символов: {}, длина кода: {}".format(len(code), len(encoded)))
