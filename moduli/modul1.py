import time

print('Начало ждем 5 секунд')
time.sleep(5)

print('конец программы')



# Импорт всех классов
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

# Глобальные настройки
Window.size = (250, 200)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = "Конвертер"


class MyApp(App):
	
	# Создание всех виджетов (объектов)
	def __init__(self):
		super().__init__()
		self.label = Label(text='Конвертер')
		self.miles = Label(text='Мили')
		self.metres = Label(text='Метры')
		self.santimetres = Label(text='Сантиметры')
		self.input_data = TextInput(hint_text='Введите значение (км)', multiline=False)
		self.input_data.bind(text=self.on_text) # Добавляем обработчик события

	# Получаем данные и производит их конвертацию
	def on_text(self, *args):
		data = self.input_data.text
		if data.isnumeric():
			self.miles.text = 'Мили: ' + str(float(data) * 0.62)
			self.metres.text = 'Метры: ' + str(float(data) * 1000)
			self.santimetres.text = 'Сантиметры: ' + str(float(data) * 100000)
		else:
			self.input_data.text = ''

	# Основной метод для построения программы
	def build(self):
		# Все объекты будем помещать в один общий слой
		box = BoxLayout(orientation='vertical')
		box.add_widget(self.label)
		box.add_widget(self.input_data)
		box.add_widget(self.miles)
		box.add_widget(self.metres)
		box.add_widget(self.santimetres)

		return box


# Запуск проекта
if __name__ == "__main__":
	MyApp().run()
	


from datetime import datetime , timedelta # можно сразу несколько функций

from time import sleep 

import time

past_data = datetime.today()+ timedelta(days=365)
print(past_data)

data = datetime.now()
print(data)

from modul import date

print(date)

import random
naber = random.random()
print(naber)
naber = random.random()* 100
print(naber)


import random
naber = random.randint(2,7)
print(naber)


from random import shuffle , choice

list_1 = ['1','2','3','4','5']
  
print(choice(list_1))  

a = (shuffle(list_1))

print(list_1)
print(list(range(0,11,2)))
print(randrange(0,10,2))


import os
try: 
    os .mkdir('test')
except FileExistsError:
    print('такой фаил не сущесвует')


os.rename('test', ' test 4')
os.remove('test2')



Внутри my_module.py создайте вызваннную print которая выводит текст "Я функция из my_module.py". А затем импортируйте my_module.py в другой файл.
   И вызовите его.

import modul 
print("Я функция из my_module.py")


Узнайте какая у вас операционная система с помощью модуля sys и выведите на экран имя опрационной системы.

import sys 

operating_system = sys.platform

if operating_system.startswith('win'):
    print("Операционная система: Windows")
elif operating_system.startswith('linux'):
    print("Операционная система: Linux")
elif operating_system.startswith('darwin'):
    print("Операционная система: macOS")
else:
    print("Операционная система: Неизвестно")


Через терминал передайте Python несколько аргументов, а затем выведите их на экран.

import sys

argument = sys.argv[1:]

for arguments in argument:
    print(argument)



Через Python у себя на рабочем столе создайте директорию, а внутри дериктории создайте 5 РАНДОМНЫХ файлов.



import os
import shutil
import glob
# перейти в папаку RandomFiles
os.chdir('./RandomFiles')
# добавить все файлы в данной папке в список
all_files = [x for x in os.listdir('.')]
# создать множество расширений имен файлов в этой папке
file_types = set((os.path.splitext(f)[1] for f in all_files))
for ftype in file_types:
    new_directory = ftype.replace(".", '')
    os.mkdir(new_directory)
    for fname in glob.glob(f'*.{ftype[1:]}'):
        shutil.move(fname, new_directory)




import os
from pathlib import Path
import random
list_of_extensions = ['.rst', '.txt', '.md', '.docx', '.odt', '.html', '.ppt', '.doc']
# перейти в папку RandomFiles
os.chdir('./RandomFiles')
for item in list_of_extensions:
    # создать 20 случайных файлов для каждого расширения имени
    for num in range(20):
        # пусть имя файла начинается со случайного числа от 1 до 50
        file_name = random.randint(1, 50)
        file_to_create = str(file_name) + item
        Path(file_to_create).touch()



import os 
try:
    os.mkdir("/Users/sardorhabibulaev/Desktop/курсы пайтон/moduli/modul1.py")
except FileExistsError:
    pass
    for i in range(0,5):
        f = (f"/home/sardor/рабочий стол/test/{i}txt",'w')
# with open ('data.txt') as fail:



Возьмите список имён из задания №2 и сформируйте 4 разные команды из всех участников.

import random

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", ]

random_list = random.shuffle(names)
taem = len (names) //4

results = []
for i in range(5):
    start = i * taem
    stop = start +taem
    taem_1 = names[start:stop]
    results.append(taem_1)


print(results)    

for result in results:
    print(result)


import random

# Список имен участников
participants = ['Иван', 'Мария', 'Алексей', 'Елена', 'Сергей', 'Анна', 'Дмитрий', 'Ольга']

# Формирование 4 команд из всех участников
num_teams = 4
team_size = len(participants) // num_teams  # Размер каждой команды

# Перемешивание списка участников
random.shuffle(participants)

# Формирование команд
teams = [participants[i:i+team_size] for i in range(0, len(participants), team_size)]

# Если осталось несколько участников, добавляем их к последней команде
if len(participants) % num_teams != 0:
    last_team = teams[-1]
    last_team.extend(participants[-(len(participants) % num_teams):])

# Вывод команд
for i, team in enumerate(teams):
    print(f'Команда {i+1}: {team}')




1.  Напишите программу которая будет принимать аргументы sys.argv и выводить на экран оттуда всё что передал пользователь.

import sys
argument = sys.argv[1:]
for arguments in argument:
    print(argument)



2. Спросите у пользователя 2 значения через input() а затем через модуль sys проверьте какое из 2-х значений занимает больше памяти.

import sys

num = input('напишите 1 значения ')
num1 = input ('напишите 2  значения')

size1 =sys.getsizeof(num)
size2 = sys.getsizeof(num1)

print(f'размер{size1}')
print(f'размер{size2}')

if size1>size2:
    print('size1 больше чем size2')
elif size2>size1:
    print('size2 больше чем size1')
else:
    print('они одинаковы')



3. Создайте программу которая спрашивает у пользователя число N для генерации пароля а затем генерирует ему пароль длиною N символов.

import random
import string

N = int(input("Введите число N для генерации пароля: "))

password = ''.join(random.choices(string.ascii_letters + string.digits, k=N))
print("Сгенерированный пароль:", password)


4. Создайте игру Камень-Ножницы-Бумага с Компьютером.
Где компьютер даёт вам выбрать опцию, а сам затем генерирует своё значение. 
По итогу говорит выиграли вы, проиграли или ничья.

import random

while True:
    num =input('сделай выбор камень ,ножницы,бумага:')
    num1 = ['камень','ножницы','бумага']
    num2 = random.choice(num1)
    print(f'\nВы выбрали {num},копьютер выбрал{num2}.\n')
    if num == num2:
         print(f"Оба пользователя выбрали {num}. Ничья!!")
    elif num == "камень":
        if num2 == "ножницы":
            print("Камень бьет ножницы! Вы победили!")
        else:
            print("Бумага оборачивает камень! Вы проиграли.")
    elif num == "бумага":
        if num2 == "камень":
            print("Бумага оборачивает камень! Вы победили!")
        else:
            print("Ножницы режут бумагу! Вы проиграли.")
    elif num == "ножницы":
        if num2 == "бумага":
            print("Ножницы режут бумагу! Вы победили!")
        else:
            print("Камень бьет ножницы! Вы проиграли.")
    play_again = "" 
    play_again = input("Сыграем еще? (д/н): ") 
    if play_again.lower() != "д": 
        break 


1.  Используя функцию randrange() получите псевдослучайное четное число в пределах от 6 до 12. 
Также получите число кратное пяти в пределах от 5 до 100.

import random

print(random.randrange(6,12,2))
print(random.randrange(5,100,5))


2.  Найдите модуль os и sys в google и поработайте с каждым отдельно.

import os

current_directory = os.getcwd()
print("Текущая директория:", current_directory)

import sys

num = sys.argv[1:]
print('оргумент камандной строки ', num)


3. Определить дату, которая наступит через 1000 дней от текущей даты

from datetime import datetime, timedelta

data_new = datetime.now()
data_new1 = data_new + timedelta(days=1000)
print('дата через 1000 дней ')
print(data_new1.date())


Повторение

1. С ПОМОЩЬЮ ЦИКЛА ПРОЙДИТЕ ПО ЛИСТУ NUMBERS И ВЫВОДИТЕ НА ЭКРАН СУММУ ДВУХ СОСЕДНИХ ЧИСЕЛ.

nuber = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]

for i in range(len(nuber)- 1):
    sun_of = nuber[i] + nuber[i+1]
print(f'Сумма строки {nuber[i]} и {nuber[i+1]} и {sun_of} ')

for i in range(len(numbers) - 1):
    sum_of_neighbors = numbers[i] + numbers[i + 1]
    print(f"Сумма чисел {numbers[i]} и {numbers[i + 1]}: {sum_of_neighbors}")


 ЗАДАНИЕ 2:
В PYTHON ЕСТЬ МОДУЛЬ DATETIME А В МОДУЛЕ ЕСТЬ ОСОБЕННЫЕ ФУНКЦИИ КОТОРЫЕ ПОКАЗЫВАЮТ НАСТОЯЩЕЕ ВРЕМЯ.
С ПОМОЩЬЮ МОДУЛЯ DATETIME ВЫВЕДИТЕ НА ЭКРАН СКОЛЬКО ВРЕМЕНИ В ДАННЫЙ МОМЕНТ.

from datetime import datetime
current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S")
print("Текущее время:", formatted_time)



# ЗАДАНИЕ 3:
В PYTHON ЕСТЬ МОДУЛЬ TIME, С ПОМОЩЬЮ НЕГО МОЖНО ОТПРАВЛЯТЬ ПРОГРАММУ В СОН.
ЗАПУСТИТЕ ЦИКЛ FOR I IN RANGE(10) И КАЖДЫЙ ШАГ ЦИКЛА ВЫЗЫВАЙТЕ ФУНКЦИЮ МОДУЛЯ TIME КОТОРАЯ ЗАСТАВЛЯЕТ ПРОГРАММУ ЗАСНУТЬ.


import time
for i in range(10):
   print('Начало ждем 10 секунд')
   time.sleep(10)

print('конец программы')


# ЗАДАНИЕ 4:
В PYTHON ЕСТЬ ВСТРОЕННАЯ ФУНКЦИЯ КОТОРАЯ ПОЗВОЛЯЕТ ОБЪЕДИНЯТЬ ДВА СПИСКА ДЛЯ ЦИКЛА FOR.

LIST1 = [1,3,5,7,9,11,13]
LIST2 = [2,4,6,8,10,12,14]
for i , i2 in zip(LIST1,LIST2):
    print(i,i2)


5.  ЗАПУСТИТЕ ЦИКЛ FOR С ДВУМЯ ПЕРЕМЕННЫМИ КОТОРЫЕ БУДУТ ПРОХОДИТЬ ПО LIST1 И LIST2 ОДНОВРЕМЕННО И ВЫВОДИТЕ ЭТИ ПЕРЕМЕННЫЕ НА ЭКРАН.

LIST1 = [1,3,5,7,9,11,13]
LIST2 = [2,4,6,8,10,12,14]
for i , i2 in zip(LIST1,LIST2):
    print(i,i2)

def my_fun():
    print('hello wirld')
my_fun()


def my_fun():
    print ( ' hello')
    my_fun(a , b)
    return a + b
my_fun
   

import random
import string


def test():
    N = int(input("Введите число N для генерации пароля: "))
    return N


def my_func(N):
    print(N)
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=N))
    print("Сгенерированный пароль:", password)
    
n = test()

func = my_func(n)



def my_fun():
    print('моя первая програма')
num1 = int(input('ведите первое число'))
num2 = int(input('ведите второе число'))
operation = input('выберите операцию(+,- ,*, /, //)')
if operation =='+':
    print ('result',num1+num2)
elif operation ==  '-':
    print('result',num1- num2)
elif operation == '*':
    print('resul', num1*num2)
elif operation == '/':
    print('result, num1/num2')
elif operation == '%':
    print('result,num1%num2')
elif operation == '//':
    print('result,12num1//mun2')

my_fun()


text 1

def fun():
    mid = len(list_1) // 2
    left_half = list_1[:mid]
    right_half = list_1[mid:]
    print(mid)
    left_half.reverse()
    right_half.reverse()
    rusult = left_half.extend(right_half)
    print(left_half,right_half)
list_1 = ['name', 'age', '1', '19']
fun()

def list_1():
    a = ['name', 'age', '1', '19']
    return a

a = list_1()
# print(a)

func(a)



#  Создайте функцию которая генерирует 10 чисел Фибоначчи: 
n = 1,1,2,3,5,8,13,21,34,...

fib1 =1
fib2 = 1
n = (input('Номер элемента ряда Фибоначчи:'))
n = int (n) - 2
i = 0 
while i < n  - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    i = i + 1
    print('Значение этого элемента:', fib2)


def fibonaci(n):
    if n in (1,2):
        return 1
    return fibonaci(n - 1) +(n - 2)
print(fibonaci(10))


def generate_fibonacci(n):
    fibonacci_seq = [1, 1] 
    while len(fibonacci_seq) < n:
        next_num = fibonacci_seq[-1] + fibonacci_seq[-2]  
        fibonacci_seq.append(next_num)  
    return fibonacci_seq

fibonacci_numbers = generate_fibonacci(10)
print(fibonacci_numbers)

def fib_number(numbers):
    
    for i in range(10):
        sum_result = numbers[i] + numbers[i+1]
        numbers.append(sum_result)
    print(numbers)

num = [1,1]

fib_number(num)



def generate_fibonacci(n):
    fibonacci_seq = [1, 1] 
    while len(fibonacci_seq) < n:
        next_num = fibonacci_seq[-1] + fibonacci_seq[-2]  
        fibonacci_seq.append(next_num)  
    return fibonacci_seq

fibonacci_numbers = generate_fibonacci(10)
print(fibonacci_numbers)


def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
num = list(fib(10))
print(num)


def fib_number(numbers):
    
    for i in range(10):
        sum_result = numbers[i] + numbers[i+1]
        numbers.append(sum_result)
    print(numbers)

num = [1,1]

fib_number(num)


def generate_fibonacci():
    fibonacci_sequence = [1, 1]  # Начальные два числа Фибоначчи
    count = 2  # Текущий счетчик

    while count < 10:  # Генерируем 10 чисел Фибоначчи
        next_number = fibonacci_sequence[count - 1] + fibonacci_sequence[count - 2]
        fibonacci_sequence.append(next_number)
        count += 1

    return fibonacci_sequence


fibonacci_numbers = generate_fibonacci()
print(fibonacci_numbers)




3. Создайте функцию сложения, затем функцию вычитания двух чисел...
Создайте 3-ю функцию которая вызывает первые 2 внутри себя.

def fun1(a, b):
    return a +b

def fun2 (a, b):
    return a -b

def fun3(a, b):
    fun1(2, 3)
    fun2(3, 4)
    print(fun1(2,3))
    print (fun2(3,4))
fun3()


def sl(a,b):
    return a+b

def vch(a,b):
    return a-b

def voz(a,b):
    slojenia=sl(a,b)
    vych=vch(a,b)
    return slojenia,vych

num=21
num1=44

print(voz(num,num1))



1. Спросите у пользователя имя файла.
Создайте функцию которая создаёт файл с именем которое передал пользователь.
Присвойте ИМЯ функции к переменной и вызывайте функцию через переменную.

def fun1():
    num1 = input('Введите имя фаила ')
    with open((num1 + '.txt'), 'w') as f:
        pass
fun_name = fun1
fun_name()
    


2. Представьте Вы работаете в Мобильной Компании и вас попросили создать генератор номеров.
Создайте функцию gen_number() которая генерирует телефонный номер с кодом 0444 _ _ _ _ _ _. 
Номера которые вы можете генерировать могут содержать в себе только числа 145790. Пример: 0444150971 0444111777 0444457901

import random

def gen_naber():

    code = '0444'
    naber = ''
    for _ in range(6):
        digit = random.choice('145790')
        naber +=digit

        return code + naber
    generated_number = gen_naber()
    print(generated_number)

import random

def gen_number():
    code = "0444"
    number = ""
    for _ in range(6):
        digit = random.choice("145790")
        number += digit

    return code + number

# Пример использования
generated_number = gen_number()
print(generated_number)




amount = 50000
percentage = 15

result = amount - (amount * percentage / 100)
print(result)


1.  Создайте 4 функции: add(), substract(), multiply(), divide()
которые будут принимать по 2 аргумента и возвращать результат: сложения,
вычитания, умножения и деления. 

def add(a,b):
    return a + b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a *b
def divide(a,b):
    return  a/b
print(add)
print(substract)
print(multiply)
print(divide)


Написать Функцию которая принимает предложение как аргумент,
считает количество букв и возвращает сколько символов он ввёл. НЕ ИСПОЛЬЗОВАТЬ функцию len()


def count_text(text):
    count = 0
    for i in text:
        count += 1

        return count
    text = 'text'
    print(count_text(text))


Напишите функцию которая спрашивает у вас чтобы вы хотели заказать покушать и выпить.
А затем записывает это всё в файл на рабочем столе menu.txt

def order_menu():
    food = input('Введите что вы хотите покушать ')
    drink = input('Введите что вы хотите попить ')
    desktop_path = "~/Desktop/menu.txt"
    with open('menu.txt') as fail:
        fail.write(f'Еда: {food}\n')
        fail.write(f'Пить: {drink}\n')
        print("Ваш заказ был записан в файл 'menu.txt' на рабочем столе.")

order_menu()




Создайте функцию которая принимает слово и создаёт файл с таким именем в той же директории, где был запущен Ваш .py файл.

file=input('введите имя файда: ')

def file_f(file):
    file_1=open(f'{file}.txt','w')
    file_1.close()

file_f(file)


Создайте 2 функции где одна функция вложена в другую.
Главная функция должна выводить на экран текст: "Я главная функция". 
А вложенная функция должна выводить на экран: "Я вложенная функция.

def num():
    print('Я главаная функция')
    def num1():
        print('Я вложеная функция')


    num1()

num()
        


Создайте функцию которая принмает тип данных dictionary, но возвращает
два Tuple в одном из них все ключи, в другом только значения.


Напишите программу которая определяет ПРОСТЫЕ ЧИСЛА. Простое число - это число которое делится только на себя и на 1.

def nuber():
    num = int(input('Введите число'))
    if num % 1 == 0:
        return True
    else:
        return False
print(2/2)


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Ввод числа от пользователя
num = int(input("Введите число: "))

if is_prime(num):
    print(num, "является простым числом.")
else:
    print(num, "не является простым числом.")


def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a

print(is_prime(int(input("Enter a number: "))))


Напишите функцию которая принимает 2 аргумента.
Эти аргументы могут быть любого типа данных но функция должна Вам вернуть эти аргументы как тип данных List.


def returne_as_list(arg1,arg2):
    result = [arg1,arg2]
    return result
arg1 = 10
arg2 = 'hello'
result_list = returne_as_list(arg1, arg2)
print(result_list)


Напишите функцию которая спрашивает у пользователя число и выводит
ему на экран именно столько строк самой себя как текст.

def line ():
    nuber = int(input('Введите число: '))
    for _ in range(nuber):
        print('line()')

line()



Создайте функцию которая принимает Имя пользователя и его зарплату и возвращает
это строкой как: ИМЯ - ЗАРПЛАТА. Если в функции не была указана зарплата - подставьте её сами. 
Значение по умолчанию - 5000.

def format_salary(name, salary=5000):
    return f"{name} - {salary}"


username = input("Введите имя пользователя: ")
user_salary = input("Введите зарплату пользователя (если не указано, будет использовано значение по умолчанию): ")

if user_salary:
    formatted = format_salary(username, int(user_salary))
else:
    formatted = format_salary(username)

print(formatted)

Напишите функцию которая спрашивает число N и генерирует вам List состоящий из N разных элементов.

def generate_list():
    n = int(input("Введите число N: "))
    numbers = []
    for i in range(1, n + 1):
        element = input(f"Введите элемент {i}: ")
        numbers.append(element)
    return numbers
result_list = generate_list()
print(result_list)


user_name = input()
user_age = ()
user_city = ()

def func (name, age = 0,citi=''):
    if age == 0:
        print('Вы зареганы')
    if not citi:
        print('Добавте город')
    return f'Имя{name}-Возраст: {age}-Город:{citi}'

print(func(age = user_age,name = user_name,citi = user_city))        



def func(**kwargs):
    func(name =  'sardor')


def main(namber):
    print(namber)
    if namber== 0 :
        return namber
    else:
        main(namber+1)
main(-20)


def main(nuber):
    print(nuber)
    if nuber == 0:
        return nuber
    else:
        main(nuber-1)
main(10)        


def func(x,y):
    return x + y
a = lambda x,y: x + y
print(func(1,5))
print(a(2,5))


import time
def decarator(main_func):
    def time_func(*args,**kwargs):
        start_time = time.time() 
        print() 


def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper

@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text

webpage = fetch_webpage('https://google.com')
print(webpage)


from datetime import datetime
def decorator (main func):
    def time func (*args,kwargs):
        start time = datetime. now()
    result
    main func(*args, **kwargs)
    end _time = datetime .now()
    time result
    end time
    start time
    print (f'work programma {time result}')
    return result
    return time func()
    @decorator
    def func()
    print|' hello D


def set_remove(set_1):
    a = set_1.pop()
    print(a)
    set_remove(set_1)
s = {1,2,3,4,5,6,7,87,9,0}

set_remove(set_1=s)    

text 4

def set_remove(set_1):
    if not set_1:
        return
    a = set_1.pop()
    print(a)
    set_remove(set_1)


s = {1,2,3,4,5,6,7,8,9}


set_remove(set_1=s)



if not s:  # Проверяем, что множество не пустое
    return

    print("Множество:", s)
element = s.pop()  # Удаляем один элемент из множества
    print("Удален элемент:", element)

    remove_elements_recursive(s)  # Рекурсивно вызываем функцию с обновленным множеством

# Пример использования
    my_set = {1, 2, 3, 4, 5}
    remove_elements_recursive(my_set)



Написать lambda которая получает сколько дней ПРОШЛО с нового года как параметр и говорит пользователю сколько дней ОСТАЛОСЬ до нового года.

days_left = lambda days_passed: 365 - days_passed
days_passed = 150
days_remaining = days_left(days_passed)
print(f"До Нового года осталось {days_remaining} дней.")


Написать lambda которая принимает 3 параметра и умножает все параметры между собой. Функция должна вернуть строку: "Объём бассейна " и значение которое получилось.

x = 2
y = 3
z = 4

print(f"Объём бассейна {x * y * z}")



Напишите функцию которая генерирует 100 рандомных чисел в диапазоне от 10 до 50 и возвращает их в листе.
Напишите ДЕКОРАТОР для этой функции которая удалит все дубликаты в первой функции и вернёт всё так же лист.

import random
def func_decarator(function):
    def inner_func():
        func = function
        b = []
        for i in func:
            if i in b:
                continue
            elif noti in b:
                b.append(i)
                return b
            return inner_func
        func_decarator()
def random_list():
               return random.choices(range(10, 51), k = 100)
print(random_list())

Напишите функцию которая спрашивает у пользователя login и password. 
Напишите декоратор который шифрует эти данные и возвращает вам зашифрованные данные.
(Можете воспользоваться функцией ord и char, можете загуглить...)








Создайте lambda функцию которая принимает одно число и возвращает это число умноженное на 1.185. Вам дан список 

def rec(c):
    if len(s) == 0:
        return s 
    for valuein s:
    a = []
    a.append(valuein)
    break
s.discard(a[0])
return rec(s)
print(rec(



def name_decarator(func):
    def wrapper(num):
        print('ghfjdk')
        func(*args,**kwargs)
        print('end dekarator')
        return wrapper
    
    @name_decarator
def print_name (num):
    print(num+1)

print_name(1)  



from datetime import datetime

def derector(func):
    def wrapper(*args,**kwargs):
        start_time = datetime.now()
        result = func(*args,**kwargs)
        print (start_time - datetime.now())
        return result
    return wrapper


@derector
def my_func():
    list_1 = list(range(1,50000))

    print(list_1)

my_func() 






def regis():
    login = input('rfedwefrvf')
    password = input('kljhjgvhbj')
    return login,password

func = regis()
def decorator(redistor):
    def wrapper(*args,**kwargs):
        print(redistor(*args,**kwargs))


        return wrapper
    

@decorator
def main ():
    print('hello')    
    
main()    




def decorator(redistor):
    def wrapper(*args, **kwargs):
        print(redistor(*args, **kwargs))
    return wrapper
login = input('Введите логин: ')
password = input('Введите пароль: ')
def regis():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    return login, password


def decorator(redistor):
    def wrapper(*args, **kwargs):
        print(redistor(*args, **kwargs))
    return wrapper


@decorator
def main():
    print('hello')


main()


def encrypt_data(data):
    encrypted_data = ""
    for char in data:
        encrypted_char = chr(ord(char) + 1)  # Сдвигаем символ на 1 позицию в таблице ASCII
        encrypted_data += encrypted_char
    return encrypted_data


def get_login_password():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    return login, password


def encrypt_decorator(func):
    def wrapper():
        login, password = func()
        encrypted_login = encrypt_data(login)
        encrypted_password = encrypt_data(password)
        return encrypted_login, encrypted_password
    return wrapper


@encrypt_decorator
def get_encrypted_login_password():
    return get_login_password()


encrypted_login, encrypted_password = get_encrypted_login_password()
print("Зашифрованный логин:", encrypted_login)
print("Зашифрованный пароль:", encrypted_password)

def encrypt_data(data):
    return ''.join(chr(ord(char) + 1) for char in data)


def encrypt_decorator(func):
    def wrapper():
        login, password = func()
        encrypted_login = encrypt_data(login)
        encrypted_password = encrypt_data(password)
        return encrypted_login, encrypted_password
    return wrapper


@encrypt_decorator
def get_login_password():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    return login, password


encrypted_login, encrypted_password = get_login_password()
print("Зашифрованный логин:", encrypted_login)
print("Зашифрованный пароль:", encrypted_password)



def decorator(registration):
    def wrapper():
        login = input("Введите логин: ")
        password = input('Введите пароль: ')

        login_result = [ord(i) for i in login]
        password_result = [ord(i) for i in password]
        return registration(login_result, password_result)


    return wrapper


@decorator
def main(login, password):
    
    print(f'Зашифрованный логин {login}')
    print(f'Зашифрованный пароль {password}')

main()


l = [1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
for i in l:
    a = lambda num: num*1.185
    print(a(i))




def func(num):
    if num < 0:
        return
    if num % 2 != 0:
        print(num)
        result = func(num -1)
        return result
    
func(566)    


Создайте модуль с функцией, которая принимает два аргумента: имя и возраст, и выводит сообщение
вида "Привет, {имя}! Тебе {возраст} лет." Импортируйте эту функцию в основной скрипт и вызовите ее с разными значениями аргументов.


def  greet (name,age):
    print(f'имя{name,}возраст{age}')



from greetings import greet
greet("Sardor",45)
greet("nux",34)
greet('Any',22)







Создайте модуль с функцией, которая принимает список чисел и возвращает сумму всех чисел. 
Импортируйте эту функцию в основной скрипт и вызовите ее с различными списками чисел.



