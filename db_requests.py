import sqlite3


# Функция выполняет запрос к базе данных, на вход
# получает имя БД и Фамилию пользователя, которого надо найти.
# Возвращает информацию о пользователях в виде списка кортежей.
def get_user_by_lastname(db_name, lastname):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'SELECT * FROM Users WHERE user_lastname = ? ORDER BY user_firstname, user_middlename',
		(str(lastname),)
		)

	data = cursor.fetchall()
	connection.close()

	return data


# Функция выполняет запрос к базе данных, на вход
# получает имя БД и Личный номер (идентификатор) пользователя, которого надо найти.
# Возвращает информацию о пользователе в виде списка кортежей.
def get_user_by_id(db_name, user_id):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'SELECT * FROM Users WHERE user_id = ?',
		(str(user_id),)
		)

	data = cursor.fetchall()
	connection.close()

	return data


# Функция выполняет запрос к базе данных, на вход
# получает имя БД и Название книги, которую надо найти.
# Возвращает информацию о книгах в виде списка кортежей.
def get_book_by_title(db_name, title):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'SELECT * FROM Books WHERE book_title = ?',
		(str(title),)
		)

	data = cursor.fetchall()
	connection.close()

	return data


# Функция выполняет запрос к базе данных, на вход
# получает имя БД и Номер идентификатор книги, которую надо найти.
# Возвращает информацию о книге в виде списка кортежей.
def get_book_by_id(db_name, book_id):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'SELECT * FROM Books WHERE book_id = ?',
		(str(book_id),)
		)

	data = cursor.fetchall()
	connection.close()

	return data


# Функция выполняет запрос к базе данных, на вход
# получает имя БД и информацию о пользователе, которого надо добавить.
# Возвращает информацию о пользователе в виде кортежа.
def add_new_user(db_name, info):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	# Запрос с записью нового пользователя
	cursor.execute(
		'INSERT INTO Users (user_lastname, user_firstname, user_middlename, user_phone_number) VALUES (?, ?, ?, ?)',
		info
		)

	connection.commit()
	connection.close()

	return None


# Функция выполняет запрос к базе данных, на вход
# получает имя БД и информацию о пользователе, которого
# надо удалить. Возвращает None.
def delete_user(db_name, user):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'DELETE FROM Users WHERE user_id = ?',
		(str(user[0]),)
		)

	connection.commit()
	connection.close()

	return None


# Функция выполняет запрос к базе данных, на вход
# получает имя БД и информацию о книге, которую надо добавить.
# Возвращает информацию о книге в виде кортежа.
def add_new_book(db_name, info):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'INSERT INTO Books (book_author_lastname, book_author_firstname, book_author_middlename, book_title, book_publishing_year) VALUES (?, ?, ?, ?, ?)',
		info
		)

	connection.commit()
	connection.close()

	return info


# Функция выполняет запрос к базе данных, на вход
# получает имя БД и информацию о книге, которую
# надо удалить. Возвращает None.
def delete_book(db_name, book):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'DELETE FROM Books WHERE book_id = ?',
		(str(book[0]),)
		)

	connection.commit()
	connection.close()

	return None


# Функция выполняет запрос к базе данных и записывает в
# таблицу с информацией об аренде книг новое событие.
# На вход получает имя БД, информацию о книге, которую арендует пользователь, и
# информацию о пользователе. Возвращает None.
def loan_book(db_name, user, book):
	loan_start_date = "2024-08-08"

	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'INSERT INTO Loans (user_id, book_id, loan_start_date) VALUES (?, ?, ?)',
		(str(user[0]), str(book[0]), loan_start_date)
		)

	connection.commit()
	connection.close()

	return None


# Функция выполняет запрос к базе данных и обновляет запись в
# таблице с информацией об аренде книг, добавляя дату сдачи книги.
# На вход получает имя БД и информацию о записи об аренде книги. 
# Возвращает None.
def return_book(db_name, loan):
	loan_end_date = "2024-10-10"

	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute(
		'UPDATE Loans SET loan_end_date = ? WHERE loan_id = ?',
		(loan_end_date, str(loan[0]))
		)

	connection.commit()
	connection.close()

	return None


# Функция получает на вход название БД и информацию о пользователе
# и возвращает информацию о еще не сданных пользователем книгах
# (книгах "на руках") в виде списка кортежей.
def get_loaned_books(db_name, user):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	query_line = ['SELECT Loans.loan_id,',
				  'Books.book_author_lastname,',
				  'Books.book_title,',
				  'Books.book_publishing_year,',
				  'Loans.loan_start_date',
				  'FROM Books',
				  'RIGHT JOIN Loans ON Books.book_id = Loans.book_id',
				  'WHERE Loans.user_id = ? AND Loans.loan_end_date IS NULL']

	cursor.execute(
		' '.join(query_line),
		(str(user[0]),)
		)

	data = cursor.fetchall()
	connection.close()

	return data


# Функция получает на вход название БД и информацию о пользователе
# и возвращает информацию об уже сданных пользователем книгах
# в виде списка кортежей.
def get_user_loan_history(db_name, user):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	query_line = ['SELECT Books.book_author_lastname,',
				  'Books.book_title,',
				  'Books.book_publishing_year,',
				  'Loans.loan_start_date,',
				  'Loans.loan_end_date',
				  'FROM Books',
				  'RIGHT JOIN Loans ON Books.book_id = Loans.book_id',
				  'WHERE Loans.user_id = ? AND Loans.loan_end_date IS NOT NULL']

	cursor.execute(
		' '.join(query_line),
		(str(user[0]),)
		)

	data = cursor.fetchall()
	connection.close()

	return data


# Функция получает на вход название БД и информацию о книге
# и возвращает информацию о пользователях, которые брали данную книгу раньше
# в виде списка кортежей.
def get_book_loan_history(db_name, book):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	query_line = ['SELECT Users.user_lastname,',
				  'Users.user_firstname,',
				  'Users.user_middlename,',
				  'Loans.loan_start_date,',
				  'Loans.loan_end_date',
				  'FROM Users',
				  'RIGHT JOIN Loans ON Users.user_id = Loans.user_id',
				  'WHERE Loans.book_id = ? AND Loans.loan_end_date IS NOT NULL']

	cursor.execute(
		' '.join(query_line),
		(str(book[0]),)
		)

	data = cursor.fetchall()
	connection.close()

	return data


# Функция выполняет запрос к базе данных, на вход
# получает имя БД и возвращает информацию о всех пользователях.
# Возвращает информацию о пользователях в виде списка кортежей.
def get_all_users(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute('''SELECT * FROM Users''')

	data = cursor.fetchall()
	connection.close()

	return data


def get_all_books(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute('''SELECT * FROM Books''')

	data = cursor.fetchall()
	connection.close()

	return data


def get_all_loans(db_name):
	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute('''SELECT * FROM Loans''')

	data = cursor.fetchall()
	connection.close()

	return data