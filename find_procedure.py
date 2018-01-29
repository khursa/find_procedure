
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import io
import os
import os.path

# import glob
# migrations = 'Migrations'
# files = glob.glob(os.path.join(migrations, "*.sql"))

files = []
os.chdir('Migrations')
all_files = os.listdir(os.getcwd()) 
sql = filter(lambda x: x.endswith('.sql'), all_files) 
for d in sql:
	files.append(d)

for file in files:
	print(file)
print('Amount of files: ', len(files))

new_list_odd = []
new_list_even = []
new_list_even = files
break_of_loop = False

while (len(new_list_odd) > 1 and len(new_list_even) > 1) or (len(new_list_odd) == 0 or len(new_list_even) == 0):

	search_string = input('\n' + 'Pleace enter your string: ')
	for file in new_list_even:
			file_name = str(os.path.basename(file))
			with open(file) as f:
				for line in f:
					if search_string in line:
						new_list_odd.append(file_name)
						print('\n' + 'The coincidences in file №', len(new_list_odd))
						print(file_name)		
	print('\n\n' + 'LIST OF FILES:' + '\n' + '\n'.join(new_list_odd))
	print('\n' + 'Amount of coincidences in files: ', len(new_list_odd))
	print('Amount of likely search files :' + str(len(set(new_list_odd))))

	set_of_list = set(new_list_odd)
	list_of_set = list(set_of_list)
	new_list_odd = list_of_set

	if len(new_list_odd) > 1:
		new_list_even.clear()

	if len(new_list_odd) == 1:
		break_of_loop = True

	if break_of_loop == False:
		search_string = input('\n' + 'Pleace enter your string: ')
		for file in new_list_odd:
				file_name = str(os.path.basename(file))
				with open(file) as f:
					for line in f:
						if search_string in line:
							new_list_even.append(file_name)
							print('\n' + 'The coincidences in file №', len(new_list_even))
							print(file_name)
		print('\n\n' + 'LIST OF FILES:' + '\n' + '\n'.join(new_list_even))
		print('\n' + 'Amount of coincidences in files: ', len(new_list_even))
		print('Amount of likely search files :' + str(len(set(new_list_even))))

		set_of_list = set(new_list_even)
		list_of_set = list(set_of_list)
		new_list_even = list_of_set

		if len(new_list_even) > 1:
			new_list_odd.clear()

print('\n' + 'Search file: ', file_name)