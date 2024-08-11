import functions


def user_menu(db_name, user):

	user_name = f'{user[1]} {user[2]} {user[3]}'

	while True:
		# Вывод пользовательского интерфейса
		functions.print_dividing_line()
	
		message_lines = [f'[ Пользователь: {user_name} ]\n',
						 "Выберите тип операции:\n",
						 "1. Выдать книгу по Названю",
						 "2. Выдать книгу по Номеру идентификатору",
						 "3. Вернуть книгу",
						 "4. Показать историю пользователя",
						 "5. Удалить пользователя",
						 "\n0. Отмена\n"]

		print('\n'.join(message_lines))

		user_input = str(input("Ввод: "))

		# Выход из цикла
		if user_input == "0":
			return None

		# Выдача книги пользователю по Названию
		elif user_input == "1":
			book = functions.find_book_by_title(db_name)

			if book:
				 functions.loan_book(db_name, user, book)

		# Выдача книги пользователю по Номеру идентификатору
		elif user_input == "2":
			book = functions.find_book_by_id(db_name)

			if book:
				 functions.loan_book(db_name, user, book)

		# Возврат книги пользователем
		elif user_input == "3":
			loan = functions.get_loaned_books(db_name, user)

			if loan:
				functions.return_book(db_name, user, loan)

		# История пользователя
		elif user_input == "4":
			functions.get_user_loan_history(db_name, user)

		# Удаление пользователя
		elif user_input == "5":

			user_is_deleted = functions.delete_user(db_name, user)

			# Если пользователь был удален, возврат в главное меню
			if user_is_deleted:
				return None


def book_menu(db_name, book):

	if book[3] == "-":
		book_info = f'{book[1]} {book[2][0]}. "{book[4]}" {book[5]} года изд.'

	else:
		book_info = f'{book[1]} {book[2][0]}. {book[3][0]}. "{book[4]}" {book[5]} года изд.'

	while True:
		# Вывод пользовательского интерфейса
		functions.print_dividing_line()
	
		message_lines = [f'[ Книга: {book_info} ]\n',
						 "Выберите тип операции:\n",
						 "1. Показать историю аренды книги",
						 "2. Удалить книгу",
						 "\n0. Отмена\n"]

		print('\n'.join(message_lines))

		user_input = str(input("Ввод: "))

		# Выход из цикла
		if user_input == "0":
			return None

		# История аренды книги
		elif user_input == "1":
			functions.get_book_loan_history(db_name, book)

		# Удаление книги
		elif user_input == "2":

			book_is_deleted = functions.delete_book(db_name, book)

			# Если книга была удалена, возврат в главное меню
			if book_is_deleted:
				return None


# Реализация основного меню
def main_menu(db_name):

	# Цикл работы программы
	programm_is_working = True
	while programm_is_working:

		# Вывод опций на экран
		functions.print_dividing_line()

		message_lines = ["Выберите тип операции:\n",
						 "1. Поиск пользователя по Фамилии",
						 "2. Поиск пользователя по Номеру идентификатору",
						 "3. Добавление нового пользователя",
						 "4. Поиск книг по названию",
						 "5. Поиск книги по Номеру идентификатору",
						 "6. Добавление новой книги",
						 "\n0. Выйти из программы\n"]

		print('\n'.join(message_lines))

		# Ввод и обработка пользовательского ввода
		user_input = str(input("Ввод: "))

		# Цикл для выхода из программы
		if user_input == "0":

			functions.print_dividing_line()

			user_input = str(input("Выйти из программы? [да / нет]: "))

			if user_input.strip().lower() == "да":
				
				programm_is_working = False
				functions.print_dividing_line()

		# Поиск пользователя по Фамилии
		elif user_input == "1":
			user = functions.find_user_by_name(db_name)

			if user:
				user_menu(db_name, user)

		# Поиск пользователя по id
		elif user_input == "2":
			user = functions.find_user_by_id(db_name)

			if user:
				user_menu(db_name, user)

		# Добавление нового пользователя
		elif user_input == "3":
			user = functions.add_user(db_name)

			if user:
				user_menu(db_name, user)

		# Поиск книг по названию
		elif user_input == "4":
			book = functions.find_book_by_title(db_name)
			
			if book:
				book_menu(db_name, book)

		# Поиск книги по id
		elif user_input == "5":
			book = functions.find_book_by_id(db_name)
			
			if book:
				book_menu(db_name, book)

		# Добавление новой книги
		elif user_input == "6":
			book = functions.add_book(db_name)

		# elif user_input == "7":
		# 	functions.print_all_users(db_name)

		# elif user_input == "8":
		# 	functions.print_all_books(db_name)

		# elif user_input == "9":
		# 	functions.print_all_loans(db_name)


	return None


def main():

	DATABASE_NAME = 'library.db'
	main_menu(DATABASE_NAME)


if __name__ == '__main__':
	main()