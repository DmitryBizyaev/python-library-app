import db_requests


# Блок программы, отвечающий за поиск пользователя по имени
# возвращает либо список с кортежами, которые содержат информацию
# о подходящих пользователях, либо None
def find_user_by_name(db_name):

	while True:

		# Вывод пользовательского интерфейса
		print_dividing_line()
		message_lines = ['Введите фамилию пользователя.',
						 '(Для отмены операции возврата назад введите 0)\n']
		
		print('\n\n'.join(message_lines))
		user_input = str(input("Ввод: "))

		# Преждевременный выход из цикла (выход назад)
		if user_input == "0":
			return None

		# Обработка пользовательского ввода
		elif user_input:

			data = db_requests.get_user_by_lastname(db_name, user_input)

			# Обработка не пустых данных
			if data != []:

				if len(data) > 1:
					return get_item_from_multiple(data, "пользователь")

				else:
					return data[0]

			# Обработка пустых данных
			else:
				print_dividing_line()

				print(f'Пользователи с фамилией "{user_input}" не найдены.\n')
				user_input = str(input("Для повторной попытки нажмите Enter."))


# Блок программы, отвечающий за поиск пользователя по имени
# возвращает либо список с кортежами, которые содержат информацию
# о подходящих пользователях, либо None
def find_user_by_id(db_name):

	while True:

		# Вывод пользовательского интерфейса
		print_dividing_line()
		message_lines = ['Введите номер идентификатор пользователя.',
						 '(Для отмены операции возврата назад введите 0)\n']
		
		print('\n\n'.join(message_lines))
		user_input = str(input("Ввод: "))

		# Преждевременный выход из цикла (выход назад)
		if user_input == "0":
			return None

		# Обработка пользовательского ввода
		elif user_input:

			data = db_requests.get_user_by_id(db_name, user_input)

			# Обработка не пустых данных
			if data != []:

					return data[0]

			# Обработка пустых данных
			else:
				print_dividing_line()

				print(f'Пользователи с номером идентификатором "{user_input}" не найдены.\n')
				user_input = str(input("Для повторной попытки нажмите Enter."))


def find_book_by_title(db_name):

	while True:

		# Вывод пользовательского интерфейса
		print_dividing_line()

		message_lines = ["Введите название интересующей книги",
						 "(Для отмены операции и возврата назад введите 0)\n"]

		print('\n\n'.join(message_lines))

		user_input = str(input("Ввод: "))

		if user_input == "0":
			return None

		elif user_input:
			data = db_requests.get_book_by_title(db_name, user_input)

			if data != []:
				
				if len(data) > 1:
					return get_item_from_multiple(data, "книга")

				else:
					return data[0]


def find_book_by_id(db_name):

	while True:

		# Вывод пользовательского интерфейса
		print_dividing_line()

		message_lines = ["Введите Номер идентификатор интересующей книги.",
						 "(Для отмены операции и возврата назад введите 0)\n"]

		print('\n\n'.join(message_lines))

		user_input = str(input("Ввод: "))

		if user_input == "0":
			return None

		elif user_input:
			data = db_requests.get_book_by_id(db_name, user_input)

			if data != []:
				return data[0]


# Блок программы, отвечающий за добавление пользователя в БД.
# На вход получает имя БД и возвращает None.
def add_user(db_name):

	while True:
		
		# Вывод пользовательского интерфейса
		print_dividing_line()

		message_lines = ['Введите информацию о пользователе через двойной пробел в следующем формате:',
						 'Фамилия, Имя, Отчество, Номер телефона (только цифры без +7).',
						 'Пример: Иванов  Иван  Иванович  9876543210',
						 '(Для отмены операции и возврата назад введите 0)\n']
		
		print('\n\n'.join(message_lines))
		user_input = str(input("Ввод: "))

		# Преждевременный выход из цикла
		if user_input == "0":
			return None

		# Обработка полученных данных (форматирование)
		info = tuple(user_input.strip().split('  '))

		try:
			# Вывод пользовательского интерфейса
			message_lines = ["Проверьте правильность введенных данных:\n",
							 f'ФИО Пользователя: {" ".join(info[:3])}',
							 f'Номер телефона: {info[3]}\n']
	
			print_dividing_line()
	
			print('\n'.join(message_lines))
	
			# Пользовательский ввод и обработка ввода в случае успеха.
			user_input = str(input("Данные верны? [да/нет]: "))
	
			if user_input.strip().lower() == "да":
				
				# Попытка добавления нового пользователя
				try:
					print_dividing_line()
	
					user_data = db_requests.add_new_user(db_name, info)
	
					print("Пользователь был успешно добавлен!\n")
					input("Для продолжения нажмите Enter.")
	
					return user_data
	
				except:
					print_dividing_line()
	
					print("Возникла непредвиденная ошибка, попробуйте еще раз.\n")
					input("Для продолжения нажмите Enter.")
	
			else:
				print_dividing_line()
	
				print("Пользователь не был добавлен.\n")
				input("Для продолжения нажмите Enter.")

		except:
			print_dividing_line()

			print("Некорректный ввод данных!\n")
			input("Для продолжения нажмите Enter.")


# Блок программы, отвечающий за удаление пользователя.
# На вход получает имя БД и информацию о пользователе,
# возвращает либо True, в случае успешного удаления пользователя,
# либо None, если удаление было отменено или возникла ошибка.
def delete_user(db_name, user):

	# Вывод пользовательского интерфейса
	user_name = ' '.join(user[1:4])
	user_phone = convert_phone_number(user[4])

	message_lines = ["Вы уверены, что хотите удалить данного пользователя?",
	    			 f'ФИО: {user_name}\nНомер телефона: {user_phone}',
	    			 "Для удаления введите полностью слово УДАЛИТЬ.\n"]

	print_dividing_line()

	print('\n\n'.join(message_lines))

	user_input = str(input("Ввод: "))

	# Обработка пользовательского ввода
	if user_input == "УДАЛИТЬ":

		# Попытка удаления пользователя
		try:
			db_requests.delete_user(db_name, user)

			print_dividing_line()

			print("Пользователь был успешно удален!\n")
			input("Для продолжения нажмите Enter.")

			return True

		except:
			print_dividing_line()

			print("Возникла непредвиденная ошибка.\n")
			input("Для продолжения нажмите Enter.")

			return None

	else:
		print_dividing_line()

		print("Пользователь не был удален!\n")
		input("Для продолжения нажмите Enter.")

		return None


# Блок программы, отвечающий за добавление пользователя в БД.
# На вход получает имя БД и возвращает None.
def add_book(db_name):

	while True:
		
		# Вывод пользовательского интерфейса
		print_dividing_line()

		message_lines = ["Введите информацию о книге через двойной пробел в следующем формате:",
						 "Фамилия, Имя, Отчество (Автора), Название книги, Год издания",
						 "В случае отсутствия Отчества поставьте прочерк (-)",
						 "Пример: Оруэлл  Джордж  -  1984  1999",
						 "(Для отмены операции и возврата назад введите 0)\n"]
		
		print('\n\n'.join(message_lines))
		user_input = str(input("Ввод: "))

		# Преждевременный выход из цикла
		if user_input == "0":
			return None

		# Обработка полученных данных (форматирование)
		info = tuple(user_input.strip().split('  '))

		try: 
			# Вывод пользовательского интерфейса
			message_lines = ["Проверьте правильность введенных данных:\n",
							 f'ФИО Автора: {" ".join(info[:3])}',
							 f'Название: {info[3]}',
							 f'Год издания: {info[4]}\n']

			print_dividing_line()
	
			print('\n'.join(message_lines))
	
			# Пользовательский ввод и обработка ввода в случае успеха.
			user_input = str(input("Данные верны? [да/нет]: "))
	
			if user_input.strip().lower() == "да":
				
				# Попытка добавления нового пользователя
				try:
					print_dividing_line()
	
					user_input = db_requests.add_new_book(db_name, info)
	
					print("Книга была успешно добавлена!\n")
					input("Для продолжения нажмите Enter.")
	
					return None
	
				except:
					print_dividing_line()
	
					print("Возникла непредвиденная ошибка, попробуйте еще раз.\n")
					input("Для продолжения нажмите Enter.")
	
			else:
				print_dividing_line()
	
				print("Книга не была добавлена!\n")
				input("Для продолжения нажмите Enter.")

		except:
			print_dividing_line()

			print("Некорректный ввод данных!\n")
			input("Для продолжения нажмите Enter.")


# Блок программы, отвечающий за удаление книги.
# На вход получает имя БД и информацию о книге,
# возвращает либо True, в случае успешного удаления книги,
# либо None, если удаление было отменено или возникла ошибка.
def delete_book(db_name, book):

	# Вывод пользовательского интерфейса
	print_dividing_line()
	book_author_name = ' '.join(book[1:4])

	message_lines = ["Вы уверены, что хотите удалить данную книгу?\n",
	    			 f'ФИО Автора: {book_author_name}',
	    			 f'Название: {book[4]}',
	    			 f'Год издания: {book[5]}',
	    			 "\nДля удаления введите полностью слово УДАЛИТЬ.\n"]

	print('\n'.join(message_lines))

	user_input = str(input("Ввод: "))

	# Обработка пользовательского ввода
	if user_input == "УДАЛИТЬ":

		# Попытка удаления пользователя
		try:
			db_requests.delete_book(db_name, book)

			print_dividing_line()

			print("Книга была успешно удалена!\n")
			input("Для продолжения нажмите Enter.")

			return True

		except:
			print_dividing_line()

			print("Возникла непредвиденная ошибка.\n")
			input("Для продолжения нажмите Enter.")

			return None

	else:
		print_dividing_line()

		print("Книга не была удалена!\n")
		input("Для продолжения нажмите Enter.")

		return None


# Блок программы, отвечающий за выдачу книги пользователю.
# На вход получает имя БД, информацию о книге и информацию о пользователе,
# возвращает None.
def loan_book(db_name, user, book):

	user_name = ' '.join(user[1:4])

	if book[3] == "-":
		book_author_name = f'{book[1]} {book[2][0]}.'

	else:
		book_author_name = f'{book[1]} {book[2][0]}. {book[3][0]}.'
		
	# Вывод пользовательского интерфейса
	print_dividing_line()
	message_lines = [f'[ Пользователь: {user_name} ]',
					 f'Книга: №{book[0]} - {book_author_name} "{book[4]}" ({book[5]} год изд.)\n']

	print('\n\n'.join(message_lines))

	user_input = str(input("Выдать книгу данному пользователю? [да/нет]: "))

	if user_input.strip().lower() == "да":

		try:
			db_requests.loan_book(db_name, user, book)

			print_dividing_line()

			print(f'[ Пользователь: {user_name} ]\n\n' + "Книга была успешно выдана!\n")
			input("Для продолжения нажмите Enter.")

			return None

		except:
			print_dividing_line()

			print("Возникла непредвиденная ошибка.\n")
			input("Для продолжения нажмите Enter.")

			return None

	print_dividing_line()

	print(f'[ Пользователь: {user_name} ]\n\n' + "Книга не была выдана!\n")
	input("Для продолжения нажмите Enter.")

	return None


# Блок программы, отвечающий за возврат книги пользователем.
# На вход получает имя БД, информацию о пользователе и информацию
# о записи об аренде книги пользователем. Возвращает None.
def return_book(db_name, user, loan):
	
	user_name = ' '.join(user[1:4])

	# Вывод пользовательского интерфейса
	print_dividing_line()
	message_lines = [f'[ Пользователь: {user_name} ]',
					 f'Книга: {loan[1]} "{loan[2]}" ({loan[3]} год изд.) | Во владении с {loan[4]}\n']

	print('\n\n'.join(message_lines))

	user_input = str(input("Подтвердить возврат книги? [да/нет]: "))

	if user_input.strip().lower() == "да":

		try:
			db_requests.return_book(db_name, loan)

			print_dividing_line()

			print(f'[ Пользователь: {user_name} ]\n')
			print("Книга была успешно возвращена!\n")
			input("Для продолжения нажмите Enter.")

		except:
			print_dividing_line()

			print("Возникла непредвиденная ошибка, попробуйте еще раз.\n")
			input("Для продолжения нажмите Enter.")

	else:
		print_dividing_line()

		print(f'[ Пользователь: {user_name} ]\n')
		print("Книга не была возвращена!\n")
		input("Для продолжения нажмите Enter.")

	return None


# Функция, которая выводит пользователю список объектов,
# получает от пользователя номер выбранного объекта
# и возвращает выбранный объект
# (множество объектов) -> (один объект)
def get_item_from_multiple(items, item_type):

	while True:

		# Вывод пользовательского интерфейса
		print_dividing_line()
		print("Введите номер интересующего результата.\n")

		# Вывод объектов для выбора
		for index, item in enumerate(items):

			option_line = f'{index + 1}. '

			# Обработка разных типов объектов
			if item_type == "пользователь":

				option_line += f'{(item[1] + " " + item[2] + " " + item[3]):<50} | {item[4]}'
				print(option_line)

			elif item_type == "книга":

				# Проверка на наличие у автора отчества
				if item[3] == "-":
					book_author_name = f'{item[1]} {item[2][0]}.'

				else:
					book_author_name = f'{item[1]} {item[2][0]}. {item[3][0]}.'

				option_line += f'{book_author_name:<20} | {item[4]:<40} | {item[5]} год изд.'
				print(option_line)

			elif item_type == "книга возврат":

				option_line = f'{index + 1}. {item[1]} "{item[2]}" ({item[3]} г. изд.)'
				print(f'{option_line:<50} | Во владении с {item[4]}')

			else:
				print("Неправильный тип")

		print("\n0. Отмена\n")
		user_input = str(input("Ввод: "))

		# Преждевременный выход из цикла (выход назад)
		if user_input == "0":
			return None

		# Возвращение выбранного объекта
		if user_input in [str(n + 1) for n in range(len(items))]:
			return items[int(user_input) - 1]


# Функция получает на вход имя БД и информацию о пользователе,
# возвращает ифнормацию о конкретной арендованной пользователем
# книге в виде кортежа.
def get_loaned_books(db_name, user):

	user_name = ' '.join(user[1:4])
	data = db_requests.get_loaned_books(db_name, user)

	if data != []:

		if len(data) > 1:
			return get_item_from_multiple(data, "книга возврат")

		else:
			return data[0]

	else:
		print_dividing_line()

		print(f'[ Пользователь: {user_name} ]\n')
		print("У данного пользователя нет не сданных книг!\n")
		input("Для продолжения нажмите Enter.")


# Функция выводит список книг, которые брал данный пользователь.
# Принимает на вход название БД и информацию о пользователе,
# Возвращает None.
def get_user_loan_history(db_name, user):

	user_name = ' '.join(user[1:4])

	data = db_requests.get_user_loan_history(db_name, user)

	if data != []:
		# Вывод интерфейса
		print_dividing_line()

		message_lines = [f'[ Пользователь: {user_name} ]',
						 "Пользователь брал следующие книги:\n"]

		print('\n\n'.join(message_lines))

		for idx, d in enumerate(data):
			temp = f'{idx + 1}. {d[0]} "{d[1]}" ({d[2]} г. изд.)'
			print(f'{temp:<50} | с {d[3]} по {d[4]}')

		print("\n")
		input("Для продолжения нажмите Enter.")

		return None

	else:
		print_dividing_line()

		print("Пользователь еще не брал книги!\n")
		input("Для продолжения нажмите Enter.")

		return None


# Функция выводит список пользователей, которые брали данную книгу.
# Принимает на вход название БД и информацию о книге,
# Возвращает None.
def get_book_loan_history(db_name, book):

	data = db_requests.get_book_loan_history(db_name, book)

	if data != []:
		# Вывод интерфейса
		print_dividing_line()

		print("Данную книгу брали следующие пользователи:\n")

		for idx, d in enumerate(data):
			temp = f'{idx + 1}. {" ".join(d[:3])}'
			print(f'{temp:<50} | с {d[3]} по {d[4]}')

		print("\n")
		input("Для продолжения нажмите Enter.")

		return None

	else:
		print_dividing_line()

		print("Данную книгу еще никто не брал!\n")
		input("Для продолжения нажмите Enter.")

		return None


# Функция выводит полный список пользователей
def print_all_users(db_name):

	data = db_requests.get_all_users(db_name)

	print_dividing_line()

	print(f' {"№":<5} | {"ФИО Пользователя":<50} | {"Номер телефона":<20}')
	print("-" * 7 + "|" + "-" * 52 + "|" + "-" * 19)

	for d in data:
		ph_num = convert_phone_number(d[4])
		print(f' {d[0]:<5} | {(d[1] + " " + d[2] + " " + d[3]):<50} | {ph_num:<20}')

	return None


# # Функция выводит полный список книг
# def print_all_books(db_name):

# 	data = db_requests.get_all_books(db_name)

# 	print_dividing_line()

# 	print(f' {"№":<5} | {"Автор":<30} | {"Название":<30} | {"Год изд":<7}')
# 	print("-" * 7 + "|" + "-" * 32 + "|" + "-" * 32 + "|" + "-" * 9)


# 	for d in data:

# 		if d[3] == "-":
# 			book_author_name = f'{d[1]} {d[2]}'

# 		else:
# 			book_author_name = f'{d[1]} {d[2]} {d[3]}'

# 		print(f' {d[0]:<5} | {book_author_name:<30} | {d[4]:<30} | {d[5]:<7}')

# 	return None


# def print_all_loans(db_name):

# 	data = db_requests.get_all_loans(db_name)

# 	print_dividing_line()

# 	for d in data:
# 		print(d)


# Функция выводит разделительную черту, для отделения элементов
# пользовательского интерфейса
def print_dividing_line():
	print('\n' + '-' * 83 + '\n')


# Функция переводит используемый в БД формат номера телефона в
# более понятный (визуально)
def convert_phone_number(phone_number):
	ph_num = str(phone_number)
	result = ['+7',
			  f'({ph_num[:3]})',
			  f'{ph_num[3:6]}-{ph_num[6:8]}-{ph_num[8:]}']

	return ' '.join(result)