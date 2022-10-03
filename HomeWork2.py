#1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример: - 6782 -> 23
#         - 0,56 -> 11
numb = float(input('Введите вещественное число\n'))
numb_len = len(str(numb)) - 1
numb_cel = int(numb)
numb_cel_len = len(str(numb_cel))
numb_dr_len = numb_len - numb_cel_len
numb_dr = int(round(numb - int(numb), numb_dr_len) * (10 ** numb_dr_len))
sum = 0
while numb_cel > 0:
    sum += numb_cel % 10
    numb_cel //= 10
while numb_dr > 0:
    sum += numb_dr % 10
    numb_dr //= 10
print(f'Сумма цифр числа {numb} равна {int(sum)}')
print('**********************************************')


#2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
numbN = int(input('Введите число больше нуля \n'))
if numbN <= 0:
    print('Необходимо ввести положительное число! \n ')
else:
    pr = 1
    listN = []
    for i in range(1, numbN+1):
        pr *= i
        listN.append(pr)
    print(listN)
print('**********************************************')


#3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.
numbPosl = int(input('Введите количество чисел последовательности \n'))
if numbPosl <= 0:
    print('Необходимо ввести положительное число! \n ')
else:
    sum = 0
    listN = []
    for i in range(1, numbPosl+1):
        membList = round((1 + 1/i) ** i, 2)
        listN.append(membList)
        sum += membList
    print(f'Последовательность: {listN}, сумма чисел последовательности равна {sum}')
print('**********************************************')


#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
import random
numbN = int(input('Введите количество элементов списка \n'))
if numbN <= 0:
    print('Введите положительное число!\n')
else:
    listN = []
    for i in range(numbN):
        listN.append(random.randint(-numbN,numbN))
    print(f'Исходный список: {listN}')
    multi = 1
    flag = False
    filePos = open('file.txt', 'r', encoding='utf-8')
    for line in filePos:
        if int(line) <= numbN:
            multi *= listN[int(line)-1]
            flag = True
    filePos.close()
    if flag:
        print(f'Произведие равно {multi}')
    else:
        print('Файл file.txt содержит некорректные данные')
print('**********************************************')

#5. Реализуйте алгоритм перемешивания списка
import random
lenList = int(input('Введите количество элементов списка \n'))
myList = []
print('Введите элементы списка, разделяя их клавишей Enter')
for i in range(lenList):
    myList.append(input())
print(f'Исходный список: {myList}')
# 1-й вариант
#random.shuffle(myList)
#print(f'Перемешанный список: {myList}')
# 2-й вариант
newList = []
while lenList > 0:
    ind = random.randint(0,lenList-1)
    newList.append(myList[ind])
    del myList[ind]
    lenList -= 1
print(f'Перемешанный список: {newList}')
print('**********************************************')