# a=12

# if a>12:
#     print(a)
# elif a<12:
#     print(a-1)
# else:
#     print(a+10)


# a = 20
# b = "мне сколько лет "
# print(b,a)

# name= 'сардор'
# a = "меня зовут"

# print(a + name)


# traffic_light = "Черный"

# if traffic_light == "Зеленый":  начала условий с if переводиться как если 
#     print ("Зеленый свет,ехать можно")

# elif traffic_light == "Желтый":  продолжаем с elif продолжаем как противном случаии 
#     print("Желтый свет,надо подождать")
# elif traffic_light == "Красный":
#     print ("Красный свет,стоять надо")
# else:   если условия выше не работает сработает на else 
#     print ("Такого цвета в светафоре нет")

# a =15 

# if a/5 == 3:
#     print(a,'делиться на 5')

# a = 11

# if a*2 == 15:
#     print(a,"Умноженная на 2 равняеться 30")
# else:
#     print(a,"Умноженная на 2 не ровняеться 30")

# a =34 
# if a%6 == 0:
#     print("Делиться на 6 без остатка ")
# else:
#     print("Не делиться на 6 без остатка")

# and 2 условия должны стработать тру , or 1 условий должен сработать 
# age = 99
# if age >12 and age <= 18:
#     print("Вход разрешен")
# # elif age > 100
# # print("Возраст не может быть 100 лет")
# elif age <0 or age >101:
#     print("Некорректный возраст ")
# else:
#     print("Вход запрещен")

# admin_login = "admin"
# admin_password = "123"

# moderator_login = "moder"
# moderator_password = "1234"

# if admin_login == "admin" and admin_password == "123" or  moderator_login == "moder" and moderator_password:
#     print (" Добро пожаловать на страницу админа ")
# elif  moderator_login == "moder" and moderator_password == "1234":
#     print("Добро пожаловать на страницу админа ")
# else: 
#     print ("У вас нет доступа на станицу админа ")


# Создайте 2 переменные со значениями 2**3 и 3**2 и покажите значение переменной в которой значение больше.

# a= 2**3
# b = 3**2 
# if b > a:
#     print ("b больше  ")
# elif ("a меньше "):
#     print (a<b)
# else:
#     print ("не сработало")


# У нас есть числа от 0 до 100, но не все числа разрешены!
# Разрешенённые:
# От 0 до 21
# От 57 до 100
# Как узнать что какое-то число из запрещёного диапазона?

# a = 59
# if a > 0 and a <21 or a > 57 and a < 100: 
#     print ("Разрешен")
# else: 
#     print("-")    

# Написать программу которая проверит число на несколько критериев:
# Чётное ли число?
# Делится ли число на 3 без остатка?
# Если возвести его в квадрат, больше ли оно 1000?

# a = 99
# if a%2 == 0:
#     print("число чет")
# else:
#     print("число нечетное")
# if a % 3 == 0 :
#     print('число делиться на 3 ')
# if a **2 >1000:
#     print("число ьодлбшк в квалрате 1000")

# else:
#     print("число в квадрате меньше 1000")            

# :
# Создайте условие которое будет срабатывать в любом случае

# a =10
# if a == 10 :
#     print("число равно 10")
# print (a == 10)         

# a = 12 == 13
# if  not a  :
#     print("Условия которое сработает в любом случаии ")
 


# name = input ("как тебя зовут ?")
# age = int (input("сколько тебе лет ?"))
# if age +  2 < 18:
#     print(" ты не совершенолетний")

# print("моя первая прогграмма")
# num1 = int (input("Ведите первое число" ))
# num2 = int(input("Ведите второк число"))
# operation = input("Выбери операцию (+ , - , *, /, %, //)")

# if operation == "+":
#     print("result", num1 + num2)
# elif operation == "-":
#     print("result", num1 -num2)
# elif operation == "*":
#     print("result", num1 *num2)
# elif operation == "/":
#     print("result", num1 % num2)
# elif operation == "//":
#     print("resul", num1 // num2)      
# else :
#     print("Некоректная операция ")    



# namber = 1900
# if namber % 4 == 0 and namber % 100 != 0  or namber % 400 == 0:
#     print("+")



# Напишите программу, которая запрашивает у пользователя его имя, возраст и гражданство, а затем выводит сообщение на экран, указывающее, может ли он получить гражданство в США. Для получения гражданства в США необходимо удовлетворять следующим требованиям:

# Быть старше 18 лет.
# Проживать в США не менее 5 лет (если есть статус постоянного жителя) или не менее 3 лет (если нет статуса постоянного жителя).
# Прошли тест на знание английского языка и истории США.

# nema = int(input("имя"))
# age = int (input("возраст"))
# citizenship = int(input(" гражданство"))
# is_permament =  input ("Вы имеете статус постоянного жителя США (да/нет)")

# if age != 18 or age <18:
#     print("возраст для получения гр (да/нет )")
# elif citizenship <3 or citizenship > 5 :
#     print("статус постоянного жителя ") 
# else : 
#     print(" прошли вы тест на знания англ языка (да/нет)")      


# name = input('Введите ваше имя ')
# age = int(input('Введите ваш возраст '))
# citizenship = input('Введите ваше гражданство ')
# is_permament = input('Вы имеете статус постоянного жителя США? (да/нет) ')

# if age >=18:
#     if citizenship == 'usa':
#         print('Вы уже гражданин сша')
#     else:
#         if is_permament == 'да':
#             year = int(input('Введите количество лет которую прожили в сша'))
#             if year >=5:
#                 print('Вы можете получить гражданство')
#             else:
#                 print('Вы не можете получить гражданство')
#         else:
#             year = int(input('Введите количество лет которую прожили в сша'))
#             if year <=3:
#                 english_test = input('Вы прошли тест на знание английского')
#                 if english_test == 'yes':
#                     print('Вы можете получить гражданство')
#                 else:
#                     print('Вы не можете получить гражданство')
            
#             else:
#                 print('Вы можете получить гражданство')
# else:
#     print('Вы не можете получить гражданство')




# print('Строк боятся не нужно!')

# info = 'Строки это всего лишь объекты заключённые в ковычки: )'
# print(info)

# info_2 = ''' Строка может быть заключена в ТРИ одинарные или в двойные ковычки'''.upper()
# print(info_2)


# info_3 = 'Строки - это всего лишь объекты, \
# и с ними можно работать.'.replace('объекты', 'ОБЪЕКТЫ')
# print(info_3)

# text = '12345678d'
# print(text.isalpha)
# print(text.isdigit)

# if text.isalpha():
#     print('Это буквы')
# elif text.isdigit():
#     print('Это цыфры')
# else:
#     print('Это и буквы и цифры')            



# text = 'hello world'

# if text .startswith('h'):
#     print('да, строка начинаеться с буквы h ')    
# else:
#     print('Нет, строка не начитнаеться с буквы h')    
# if text.endswith('l'):
#     print('Да, строка заканчиваеться на букву l')
# print(text.startswith("hello world"))


# name = input('Как тебя зовут')
# age = int(input('Сколько тебе лет'))
# print ('')
# print ('Привет, меня зовут ' {} ' и мне ' {}  'лет' . format ( name,age ))


# name = input(' как тебя зовут')
# age = input('сколько тебе лет')

# print('Привет, меня зовут ' + name + ' и мне ' + str(age) + ' лет')
# print('Привет меня зовут', name, 'мне', age)
# print('Привет, меня зовут {} и мне {} лет'.format(name, age))
# print(f'Привет мен зовут {name}, мне {age}')

# print('Привет', name) 



# text = 'Привет мир это проверка'
# print(text.title( ) )
# text = text.upper()
# print(text)
# print(text.lower())



# age = input('Тебе точно 18? да/нет ')
# age = age.lower()
# print(age)
# if age == 'да':

#     print('Добро пожаловать в наш клуб')

# else:
#     print('Ты не пройдешь')


# text = '01 kg 123abc'
# v= len(text)
# print(v)
# a = text.strip('ep')
# len_ = len (a)
# print(len_)
# print(a)


# text = 'г гамбург'
# a = text.strip('г')
# tittle = a.title()
# print(a)




# num = 'Самые важнык события в мире '
# num = num .count(',')
# print(num)


# num = '1','2','3','4'
# num =','.join(num)
# print(type(num))
# print(num)



# a = '123'
# print(a.isdigit())


# a = '123d'
# print(a.replace('d','4').replace('1', ' 0'))



# a = ('12',12, True, 12.12 )
# print(type(a))
# list((a))


# users= ['Adinai', 'Dastan','Ermek',]
# users2 = ['Aibek','wqerty','Elturan']
# print(users.append(123))
# result = users + users2
# print(result)
# print(users[-1])
# print(users)




# PROBLEM 0 
# Создать список и 5 вложенных кортежей.


# name = ['Sardor', "Marat",'Maga',"Idris"]
# print(name.append('Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',))


# PROBLEM 1 
# Создать Tuple из 3 элементов и вывести каждый из них по индексу


# name = ('pop','drom','dick')
# name1 = name.index('pop')
# print(name[0])
# print(name[1])
# print(name[2])


# PROBLEM 2 
# Создать Лист и заполнить его 5 РАЗНЫМИ ТИПАМИ ДАННЫХ.

# users = ['int','str','true','tuepl','formar']


# PROBLEM 3 
# 1.Создать Лист из 5 разных имён.
# 2.Создать пустую строку и через .join() соеденить пустую строку и все имена в списке

# name = ['Idris','Nxx','Sardor','Maga','Saha']
# print(name)
# str_1 = ''
# print(str_1.join(name))


# PROBLEM 4
# Создать 2 списка(List) заполнить данными, к первому списку добавить все объекты второго списка

# list_1 = [1,2,3,4,5]
# lisr_2 = [6,7,8,9,10]
# list_extend = list_1.extend(lisr_2)
# print(lisr_2)


# PROBLEM 5
# Взять Лист №1 из Google Colab и посчитать сколько раз там встречается имя "Jack"


# names =  ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
# print(names)
# print(len(names))
# print(names.pop(-1))
# print(names[-1])


# PROBLEM 6
# Удалить из Листа №1 объект "Oskar"






# PROBLEM 7
# Создать пустой лист.
# Добавить в него сначала Ваше Имя, Год Рождения, любимый Язык Программирования.
# list_1 = list()
# name = 'Adinai'
# year = 2000
# language = 'Python'

# list_2 = [name, year, language]
# print(list_2)


# PROBLEM 8
# Взять Лист №2 из Google Colab узнать индекс объекта(строки) "loop" и удалить его по 


# pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
# index_list = pythonList.index('else')
# remove = pythonList.pop(index_list)
# print(pythonList)



# PROBLEM 11
# Взять Лист №2 и вывести объекты с 1 по 3 индекс


# pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
# list_int = [0,1,2,3,4,5,6,7,8,9,10]
# print(list_int[1::2])



#  1. Проверьте, является ли строка пустой.

# my_sting = ()
# if not my_sting:
#     print('строка пустая')
# else:
#     print('сторока не пустая')    


# 2.Попросите пользователя ввести несколько чисел, разделенных запятой, и создайте список из этих чисел.

# x = 89.56238
# y = 56.2698
# print(round(x))


#3 Создайте список вещественных чисел и округлите каждое число до двух десятичных знаков.

# num1 = input('Введите число')
# resever_num1 = num1 [::-1]
# print(resever_num1) 


#4.Попросите пользователя ввести свое имя и выведите его в обратном порядке.

# num1 = input('Введите имя')
# reverse_num =num1[::-1]
# print('Ваше имя Наоборот',reverse_num)



# 7 Создайте список, содержащий 10 случайных чисел от 1 до 100, и отсортируйте его в порядке убывания.



#Создайте список чисел от 1 до 20 и замените все четные числа на строку "четное".


# numbers = [i if i % 2 != 0 else 'четное' for i in range(1, 20)]
# print(numbers)


# l = ['яблоко','груша','апельсин','банан','киви']


# if 'яблоко' in l:
#     print('Содержит')
# else:
#     print('Не содержит')


# list_1 = list(range(1,11))
# print(list_1)


# a = 'aaa oo ooo'
# b = a.strip('o')
# c = a.strip('a')
# print(c)
# print(b) 


# num2 = list(range(1,21,2)) #1) от какого числа начинаем, 2) до какого числа само число не входит, 3) шаг
# print(num2)
# num3 = list(range(0,21,2))
# print(num3)

# a = 0
# b = 7
# print(a<7)
# while a<7:
#     # if a == 5 :
#         print(a)
#         # a = a +1

# a = 0
# while a < 7:
   
#         print(a)
#         a = a + 1

# date = 10
# a = date + 15

# while date < 15:
#     print('hello') 

#     date = date + 1


# name = ['Test', 'Python3',' Java']

# num =[1,23,45,6,7,776,78,88]
# for i in num:
#     print(i , i**2)

# for i in 'hello':
#     print(i)

# a =0
# while a < 10:
#     if a == 5:
#      print('end')
#     break

# a = a +1
# print(a)


# while True:
#     name = input('Enter your name: ') 
#     if name == 'exit':
#         print('Hello', name)


# while True:
#     num1 = int (input("Ведите первое число" ) )
#     num2 = int(input("Ведите второк число"))
#     operation = input("Выбери операцию (+ , - , *, /, %, //)")

#     if operation == "+":
#         print("result", num1 + num2)
#     elif operation == "-":
#      print("result", num1 -num2)
#     elif operation == "*":
#      print("result", num1 *num2)
#     elif operation == "/":
#         print("result", num1 % num2)
#     elif operation == "//":
#         print("resul", num1 // num2)      
#     else :
#         print("Некоректная операция ")    


# while True:
#     num1 = int(input('Введи первое число '))

#     num2 = int(input('Введи второе число '))

#     operation = input('Выбери операцию (+, -, *, /): ' )

#     if operation == '+':
#         print(num1 + num2)
     
#     elif operation == '-':
#         print(num1 - num2)

#     elif operation == '*':
#         print(num1 * num2)

#     elif operation == '/':

#         if num2 != 0:
#             print(num1 / num2)
#         else:
#             print('На ноль делить нельзя')
    
#     else:
#         print('Выбери операцию из списка')

#     answer = input('Хочешь продолжить? (да/нет): ').lower()

#     if answer == 'нет':
#         break
#     elif answer == 'да':
#         continue
#     else:
#         print('Некорктный код')
#         break


# for i in range(0,20,2):
#     if i == 11:
#         break
#     print(i)

# str_1 = 'Test'
# for i in str_1:
#     if i =='e':
#         print(i)

# list_1 = [1,2,3,4,5,6,7,8,9]
# for i in list_1:
#     if i >= 5 :
#         print(i)


# for i in range(1,6):
#     print('0',i)


# a = 0 
# num = 1

# while  a < 100:
#     a = a + num
#     num = num +1
#     print(a)


# Задача 1
# Есть список:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Выведите все элементы, которые больше 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for a in a:
#     if a > 5:
#         print(a)


#Задача 2
# Есть набор чисел 
# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
# Поделить каждое число из digits на 9 и вывести на экран.


# digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)

# for digits in digits:
#     if digits/ 9:
#         print(digits)

# 3. Дан список [2,5,2,-5,7,0,1,2,-3,-2,1,3,6,3]. Найти количество положительных чисел среди них;

# num = [2,5,2,-5,7,0,1,2,-3,-2,1,3,6,3]
# list1 = []
# for i in num :
#     if i > 0:
#         list1.append(i)
#         print(len(list1))


# 4. Перемножить все не чётные значения в диапазоне от 0 до 9435


# for i in range(0 ,9435,):
#         # i *= i 
#         # print(i) 
#         if i % 2!=0 :
#                 print(i * i)



# 1. Создайте список чисел и выведите только уникальные числа (без повторений), упорядоченные по возрастанию.

# l = [ 1,2,3,4,5,6,7,89,0,]
# a = sorted(set(l))
# print(a)



# 2. Напишите программу, которая принимает строку от
# пользователя и выводит все слова, которые начинаются и заканчиваются одной и той же буквой.


# txt = input('Please input: ').split()
# for i in txt:
#     if i[0].lower() == i[-1].lower() and len(i) >= 3:
#         print(i)


# 3. Выведите на экран числа от 1 до 10 используя циклы while и for по отдельности

# for i in range(1,11):
#     print(i)
# a = 1
# while a <= 10:
#     print(a)
#     a += 1


# 4. Создайте список строк и выведите только те строки, которые содержат только цифры и буквы верхнего рег

# l = ['Hello', 'World', '123', '123HELLO', '123World', '123HelloWorld', '123HelloWorld123', '123HelloWorld123!@#']
# for i in l:
#     if i.isalnum and i.isupper():
#         print(i)


#5.  Напишите программу, которая запрашивает у пользователя числа с клавиатуры до тех пор, пока он не введет отрицательное число.
# После окончания ввода, выведите сумму всех введенных положительных чисел.
# nabers=  []
# while True:
#     num = int( input('Ведите числа с клавиатуры '))
#     if num < 0 :
#         break
#     nabers.append(num)
#     num1 = sum(filter(lambda x : x < 0 , nabers))
#     print("Сумма продлжительных чисел", num1)

# a = 0 
# while True:
#     num = int(input('Enter the number:'))
#     if num < 0:
#         print('The End')
#         break
#     elif num 0:
#         continue
#     else:
#         a+=1
#         print('Naber of enterend numbers', a)

# 6. Создайте переменную с начальным значением 10. Используя цикл while, 
# уменьшайте значение переменной на 2 на каждой итерации и выводите текущее значение переменной на экран. 
# Продолжайте цикл до тех пор, пока значение переменной не станет отрицательным.

# num = 10 
# while num>= 2:
#     print('Текущие значение переменой ', num)
#     num -= 2    


# 7. Напишите программу, которая запрашивает у пользователя числа с клавиатуры до тех пор, пока он не введет число, равное 0.
# После окончания ввода, выведите количество введенных положительных чисел.


# nabers = []
# while True:
#     num = int(input('Ведите числа с клавиатуры'))
#     if num == 0 :
#         break
#     nabers.append(num)
    
#     num1 = sum(filter(lambda x : x > -1 , nabers))
#     print("Сумма продлжительных чисел", num)

# a = 0 
# while True:
#     num = int(input('Enter the number:'))
#     if num == 0:
#         print('The End')
#         break
#     elif num< 0:
#         continue
#     else:
#         a+=1
#         print('Naber of enterend numbers', a)

# 8.  Напишите программу, которая запрашивает у пользователя пароли до тех пор, пока он не введет правильный пароль "password123".
# После успешного ввода, выведите сообщение "Доступ разрешен!".

# passowrd = ''
# a = 0 
# while a <= 5 :
#     while passowrd != 'pssowrd123':
#         passowrd = int(input('Введите пароль !'))
# print("Доступ разрешен !")


# passowrd = 'pssowrd123'
# a = 0
# while a <5:
#     passowrd_input = input('Введите пароль: ')

#     if passowrd_input == passowrd:
#         print('Пароль верный')
#         break
#     else:
#         a += 1
#         print('Пароль неверный\n')



# Напишите программу, которая считывает целое число с помощью input и выводит его квадрат, если число
# положительное, и куб, если число отрицательное.

# namber = int(input('Введите число '))
# if namber > 0 :
#     i = namber ** 2
#     print('Число в кводрате',i)    
# elif namber<0:
#     b = namber ** 3
#     print('Куб числа', b)    
# else:
#     print('Чсисло ноль')    


# Напишите программу, которая считывает список слов с помощью input и выводит только те слова, которые содержат букву "e".

# name = input('Введите слова').split()
# for i in name:
#     if 'e'in i and len (name) > 1 :
#         print(i)
# print(i) 

# Напишите программу, которая считывает список чисел с помощью input и выводит только те числа, которые делятся на 3 и 5 одновременно.

# for i in range(1,50):
#     if i%3==0 and i%5==0:
#         print(i) 

# Создайте список слов и выведите самое длинное слово из списка.

# name = ['chjedm','vrckmwxhjncm','bfekmr3jenwbrhj3jfbcrbv']
# new_name = max(name, key=len)
# print('самое длиное слово', new_name) 





# set_1 = {1,2,3,4,5,6,7,8,9}
# remove_set = set_1.discard(10)
# print(set_1)



# set_1 = {'123', 312312, '3123123'}
# # remove_set = set_1.discard(10) если обьект есть он удалит если его нет продолжит работать без ошибки
# # remove_set2 = set_1.remove(10) если обьекта нет выведет ошибку
# pop_set = set_1.pop() #удаляет один случайный обьект

# print(set_1)


# set1 = {1,2,3,4,5}
# set2 = {4,5,6,7}
# set3 = {4,10,11,}
# result = set1.intersection(set2,set3)
# print(result)

# dict = {'имя': 'сардор','возраст':19, 'професия':'програмист', 'квартира': True}
# print(dict.get('квартира','Квартира отсутсвует'))
# print(dict.get['квартира'])


#task1
# dates_of_birth = {3,10,11,13,31,21,1,10,3,5,6,6}
# dates_of_birth.discard(7)
# print(dates_of_birth)
# #task2
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# same = farm_1.intersection(farm_2)
# print(same)
# #task3
# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# dif = farm_1.difference(farm_2)
# print(dif)
# #task4
# set1 = {1,'asdasd','rwerwer',6564655, 'False'}
# set1.pop()
# print(set1)



# dict = {'имя': 'сардор','возраст':19, 'професия':'програмист', 'квартира': True}

 # key = dict.keys()
# for i in dict.values():
# items = dict.items()
# print(dict)
# for i in dict.items():
#     print(i)

# dict1 = {'jvedkn':'gbrfve','rtbevwc':'tberv'}

# dict.update(dict1)
# print(dict)

# dict['машина']= False
# print(dict)

# dict1 = {'имя': 'Элтуран', 'возраст': 19, 'профессия': 'программист', 'квартира': True}
# print(dict1.get('123', 'такого ключа нет'))
# print(dict1.setdefault('машина', False))
# print(dict1['профессия'])
# print(dict1)


# user = {
#     'user': {
#     'login': 'XXX 01',
#     'email': 'chefsardor@gmail.com',
#     'password': 'sir10',
#     'social_media': {
#             'instagram': 'XXX 01',
#             'telegram': 'XXX 01',
#             'tiktok': 'XXX 01',
#             },
#     'phone_number': [996551801108, 996501801208]
#     }
    
# }

# user1 = {
#     'login': 'admin',
#     'email': 'atosh@gmail.com',
#     'password': 'admin',
#     'socail_media': {
#             'instagram': 'admin',
#             'telegram': 'omen',
#             'tiktok': 'odmen',
#         },
#     'phone_number':[996557998182,996550073073]
    
# }
# user.update(user1 = user1)
# # # for i in user.item():
# # #     print(i)
# # print(user['user']['login'])


# dict_2 = {('1',2):'123'}
# print(dict_2)


# PROBLEM 000:
# Из Dictionary №1:
# Добавьте в меню 
#  'besh_barmak' который стоит  130 сом.

# Оказалось лагман слишком дешевый. Обновите цену на 135

# Ваш повар отвратительно готовит борщ, поэтому хотите удалить это блюдо.
# Удалить borsh


# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}

# menu['besh_barmak'] = 130
# menu['lagman']= 135
# # del menu['borsh']
# menu.pop('borsh')
# print(menu)



# PROBLEM 10:
# Из Dictionary №1:
# Добавьте в меню 
# напитки как ключ "drinks", 
# menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']
# print(menu)



# PROBLEM 020:
# Создайте SET который хранит в себе все методы  для работы  с  SET.

# Создайте второй SET который хранит в себе  методы  для работы  с  Dictionary которые вы сегодня узнали.

# Проверьте какие методы похожи у этих типов данные.

# set_methods = {
#     'add()',
#     'clear()',
#     'copy()',
#     'difference()',
#     'difference_update()',
#     'discard()',
#     'intersection()',
#     'intersection_update()',
#     'isdisjoint()',
#     'issubset()',
#     'issuperset()',
#     'pop()',
#     'remove()',
#     'symmetric_difference()',
#     'symmetric_difference_update()',
#     'union()',
#     'update()',
# }
# dict_methods = {
#     'clear()',
#     'copy()',
#     'fromkeys()',
#     'get()',
#     'items()',
#     'keys()',
#     'pop()',
#     'popitem()',
#     'setdefault()',
#     'update()',
#     'values()',
# }
# similar_methods = set_methods.intersection(dict_methods)
# print(similar_methods)

# {'copy()', 'clear()', 'update()'}



# PROBLEM 31:
# Создайте пустой словарь.

# Запустите цикл который 3 раза спросит его имя и его пароль.

# Записывайте имя пользователя как ключ, а пароль как его значение.

# num = {}

# i  == 0
# while i < 3:
#     name = input('введите имя ')
#     password = input('введите пароль')
#     num[name]= password
#     i + 1
#     print(num)


# dict_1 = {'erg':'gve','sfrsdgv':'tebrgve','grevww':'grgfeweb',}
# for key , value in dict_1.items():
#     print{f'rgrfrefr {key},gt4jrfu3fjrfnkm(value)'}

# PROBLEM 22:
# Создайте цикл который справшивает у пользователя 10 чисел и добавьте их в SET.
# Сделайте так чтобы эти данные уже никто не смог поменять позже.

# set_1 = set()
# for i in range(10):
#     num = int(input('rvrever'))
#     set_1.add(num)
#     frozenset_1 = frozenset(set_1)
#     print(type(frozenset_1))
#     print(set_1)


# PROBLEM 11:
# Есть список Южноамериканских стран
# Google Colab - 
# СПИСОК №2
# в котором Суринам встречается два раза. Необходимо написать программу,
# которая удалит дублирующуюся запись, и возвратит в результате список.


# farm_1 = {"dog", "cat", "mouse", "sheep"}






# PROBLEM 101:
# Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст: 
# suitcase = [] 
# Однако он
# может вместить всего 5 вещей.
# Положите 5 вещей в чемодан.
# Вы передумали, и решили убрать последнюю вещь.


# suitcase = [] 

# suitcase.append('safaf')
# suitcase.append('fghg')
# suitcase.append('ertre')
# suitcase.append('mh,hj')
# suitcase.append('fsdfsdf')
# print(suitcase)
# suitcase.pop(-1)
# print(suitcase)





# PROBLEM 001:
# Из Google Colab Множество 4 и 5
# Напишите код, который: Выведет новое множество, которое есть как в
# первой ферме, так и во второй.

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# fram_2 = {'cow','horse','donke','cot','dog'}
# fram_3 = farm_1.intersection_update(fram_2)
# print(fram_3)


# PROBLEM 100:
# Из Google Colab Множество 4 и 5 

# Напишите код, который выведет новое множество, состоящее из животных,
# которые есть во второй ферме, но нет в первой.

# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_1 = {"dog", "cat", "mouse", "sheep"}

# farm_3 = farm_2.difference(farm_1)
# print(farm_3)


# dict1 =  {
#     'name':'cefwd',
#     'age':30,
#     'cirty':'new yrk'
# }
# print(dict1)
# dict1['car']= False
# dict1['age']= 31
# print(dict1)
# if dict1['age']<=30:
#     print('you are young')
# else:
#     print('no')

# dict_1 = {
#         'name':'life',
#         'possword':'mide+',
#         'age':'you',
#     }
# print(dict_1)
# dict_1['possword']= 1212

# 1. Даны списки:
# list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Нужно вернуть список, который состоит из элементов, которые есть либо только в первом, либо только во втором


# list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# lis1 =[]
# list2 =[]
# for i in list_1:
#     if i not in list_2:
#         lis1.append(i)
# for i in list_2:
#     if i not in list_1:
#         list2.append(i)
# print(lis1)
# print(list2)


# 2.
# list_1 = [2, 8, 1, 2, 5, 3, 4, 6, 7, 9, 10, 8, 11, 17, 13]
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.


# list_1 = [2, 8, 1, 2, 5, 3, 4, 6, 7, 9, 10, 8, 11, 17, 13]
# seen_nabers = set()
# for  i  in list_1:
#     if i in seen_nabers:
#         print('Yes')
#     else:
#         print('NO')
#         seen_nabers.add(i)
        
3. 
# Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны по цвету. Однажды дети заинтересовались, сколько
# существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах.
# Для этого они занумеровали все цвета случайными числами от 0 до 10^8. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в оставшейся части.В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори. В следующих N строках заданы номера цветов кубиков Ани. В последних M строках номера цветов Бори.
# num = int(input('Количество цветов:'))
# baris = []
# any = []

# any_cubik = [1,2,3,4,5,6,7,8]
# bora_cubik = [11,22,3,3,45,667,77]
# any_colors= set(any_cubik)
# bora_colors = set(bora_cubik)
# i_colors = any_colors.intersection(bora_colors)
# num_common_colors = len(i_colors)
# print('Количество общих цветов', num_common_colors)

# n = 5
# m = 7

# anya = set()
# borya = set()

# for i in range(n):
#     anya.add(int(input('Enter the number Anya: ')))
# for i in range(m):
#     borya.add(int(input('Enter the number Borya: ')))
# print('Total:', len(anya.union(borya)), sorted(anya.intersection(borya)))
# print('Difference: ', len(anya.difference(borya)), sorted(anya.intersection(borya)))
# print('Difference: ', len(borya.difference(anya)), sorted(borya.intersection(anya)))


# anya_colors={2,3,213,24,5,54,53,}
# borya_colors={1,21,32,43,5,64,342,3}

# colors_result=anya_colors.intersection(borya_colors)
# only_anya_colors=anya_colors.difference(borya_colors)
# only_borya_colors=borya_colors.difference(anya_colors)


# len_result=len(colors_result)
# len_anya_colors=len(only_anya_colors)
# len_borya_colors=len(only_borya_colors)

# print(f'количество общих цаетов:  {len_result}')
# print(f'количество цветов ани:  {len_anya_colors}')
# print(f'количество цветов бори:  {len_borya_colors}')




# a= 0
# while a < 6:
#     try:
#         print('1212'+'123123')
#         a+=1
#         if a == 3:
#             print(234324+'324234234')
#             print(afsfsdf)


#     except:
#         print('цикл остановлен')
#         break


# try: #сразу закрываем try с помощью : 
#     print(23131+'123123') #пишем участок кода где возможна будет ошибка

# except TypeError: #пишем на уровне с try если try внутри условия значит и except будет 
#     # внутри условия и обязательно должны указать ошибку которую хотим обработать 

#     print('error') #сюда пишем логику после выхода ошибки


# 1. Напишите код где есть TypeError,IndexError,NameError.
# TypeError
# a = 5
# b = '10'
# c = a +b
# IndexError
# my_list = [1,2,3]
# print(my_list[3])
# NameError
# print(non_existent_variable)


# Возьмите код #1 с Classroom и создайте для него try... except... Создайте несколько except выражений для разных типов ошибок.
# try:
#     at = 10
#     wo = 20
# # except Exception as i:
#     for i  in range(-at, at):
#         try:
#             print(wo / i)
#         except ZeroDivisionError:
#             print('дедления на ноль')
# except TypeError:
#     if at > 5:
#         print("at > 5")


# Перенесите к себе код #2 с Classroom и исправьте все ошибки, сделайте так чтобы работал. 
# Если не знаете как исправить ошибку создайте для неё except выражение.
   
# lst = []
# for i in range(10):
#         lst.append(i) 

# a = list(reversed(lst))
# sls_obj = slice(0,8)
# # print(a[sls_obj])

# Перенесите к себе код #3 с Classroom и исправьте все ошибки, сделайте так чтобы код работал.
# Если не знаете как исправить ошибку создайте для неё except выражение.

# a = 0
# b = 1
# numbers = ()
# while b > a:
#     numbers += (a,)
# a += 1
# print(numbers)

# a = (0)
# b = (1)
# numbers = []
# while b > a:
#     numbers.append(b)
#     b += 1
#     break
# print(numbers)


# Дан словарь в котором ключи должны быть только строковыми объектами, но может встретиться Int, как в качестве ключа, 
# но ваша проверка только проверяет на строку и поэтому у вас выходит баг, ваша задача обработать исключением ошибку TypeError
#    Пример:

# dict_ = {'name': 'john', 'lastname': 'Snow', 12: 'age'}

# for x in dict_.keys():

#     try:
#         str(x) + 'abc'
#     except TypeError:
#         print('error')


# Напишите программу, которая просит пользователя ввести два числа.
# Затем программа должна попробовать разделить первое число на второе и вывести результат.
# Однако, необходимо учесть возможные исключения, такие как деление на ноль или ввод некорректных данных


# number = int(input('Введите 1  число '))
# number1 = int(input('Введите 2 число '))
# if number >= 0 and number1>= 0 :
#     try:
#         print('Число поделило ',number/number1)
#     except ZeroDivisionError:
#         print(ZeroDivisionError)
# else:
#     print('Не коректный вод')   

# Напишите программу, которая запрашивает у пользователя список чисел,
# разделенных запятой. Используйте конструкцию "try-except" для обработки возможных исключений, 
# связанных с некорректным форматом ввода. Если ввод корректен, программа должна вывести сумму всех чисел из списка. 
# Если возникло исключение, программа должна вывести сообщение "Ошибка: некорректный ввод списка чисел!".

# nuber = (input('Введите список чисел разделенных запятой'))#.split(',')
# try:
#     nuber1 = [float(values.strip())for values in nuber.split(',')] 
#     num1 = sum(nuber1)
#     print('Сумма чисел из списка ',num1)
# except ValueError:
#     print('Ошибка: некорректный ввод списка чисел!')


# values = input('input some comma seprated numbers:').split(',')
# try:
#     result = [int(x)for x in values]
#     print(sum(result)) 
# except ValueError:
# #     print('ValueError')

# Напишите программу, которая открывает файл "data.txt" для чтения.
# Используйте конструкцию "try-except" для обработки возможных исключений, 
# связанных с отсутствием файла или ошибками во время чтения файла.
# Если файл существует, программа должна вывести его содержимое. 
# Если возникло исключение, программа должна вывести сообщение "Ошибка: невозможно прочитать файл!".

# try:
#     with open ('data.txt','r') as fail:
#         num = fail.read()
#     print(num)  
# except FileExistsError:
#     print('фаил не найден')
# except OSError:
#     print("Ошибка: невозможно прочитать файл!")



# Напишите программу, которая открывает файл "data.txt" для записи.
# Используйте конструкцию "try-except" для обработки возможных исключений,
# связанных с ошибками во время записи в файл. Если файл успешно открыт, программа должна 
# запросить у пользователя строку и записать ее в файл. Если возникло исключение, программа 
# должна вывести сообщение "Ошибка: невозможно записать в файл!".


# try:
#     with open ('data.txt','w') as fail:
#         num = input('Введите стороку для записи: ')
#         fail.write(num)
#     print('строка успешно записана в файил')
# except OSError:
#     print("Ошибка: невозможно прочитать файл!")




# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * 2
#     return wrapper

# @decorator
# def sum_num():
#     return 5+5

# print(f'Result: {sum_num()}')


# @decorator
# def func():
#     return 4+4

# print(f'Result: {sum_num(54,23)}')



# # task8
# # Напишите функцию, которая принимает список чисел в качестве аргумента и возвращает сумму всех чисел, кратных 3. 
# # Создайте декоратор, который выводит результат работы функции в консоль. 
# # Протестируйте функцию с декоратором на произвольном списке чисел.


# def deco(func):
#     def wrapper(num):
#         result = func(num)
#         print(f"Результат: {result}")
#         return result
#     return wrapper

# @deco
# def triple(num):
#     multiples = [numbers for numbers in num if numbers % 3 == 0]
#     return multiples

    
        
# numbers1 = [1,2,3,4,5,6,67,22,34,23,4,234,23,4]
# numbers2 = [234,234,23,423,4,234,235,2345,234,624,5367,245,6,23456]

# triple(numbers1)
# triple(numbers2)

