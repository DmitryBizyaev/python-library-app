import sqlite3
import db_test_data


# Функция создает БД
def create_db(db_name):

	connection = sqlite3.connect(db_name)
	connection.close()

	return None


# Функция создает таблицу пользователей в БД
def create_table_users(db_name):

	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Users (
	user_id INTEGER PRIMARY KEY,
	user_lastname TEXT NOT NULL,
	user_firstname TEXT NOT NULL,
	user_middlename TEXT NOT NULL,
	user_phone_number INTEGER NOT NULL
	)
	''')

	connection.commit()
	connection.close()

	return None


# Функция создает таблицу книг в БД
def create_table_books(db_name):

	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Books (
	book_id INTEGER PRIMARY KEY,
	book_author_lastname TEXT NOT NULL,
	book_author_firstname TEXT NOT NULL,
	book_author_middlename TEXT,
	book_title TEXT NOT NULL,
	book_publishing_year INTEGER NOT NULL
	)
	''')

	connection.commit()
	connection.close()

	return None


# Функция создает таблицу с информацией об аренде книг
def create_table_loans(db_name):

	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	cursor.execute('''
	CREATE TABLE IF NOT EXISTS Loans (
	loan_id INTEGER PRIMARY KEY,
	user_id INTEGER NOT NULL,
	book_id INTEGER NOT NULL,
	loan_start_date DATE NOT NULL,
	loan_end_date DATE
	)
	''')

	connection.commit()
	connection.close()

	return None


# Функция заполняет таблицу пользователей в БД тестовыми данными
def fill_table_users(db_name, users_data):

	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	for data in users_data:
  		cursor.execute(
  			'INSERT INTO Users (user_lastname, user_firstname, user_middlename, user_phone_number) VALUES (?, ?, ?, ?)',
  			data)

	connection.commit()
	connection.close()

	return None


# Функция заполняет таблицу книг в БД тестовыми данными
def fill_table_books(db_name, books_data):

	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	for data in books_data:
  		cursor.execute(
  			'INSERT INTO Books (book_author_lastname, book_author_firstname, book_author_middlename, book_title, book_publishing_year) VALUES (?, ?, ?, ?, ?)',
  			data)

	connection.commit()
	connection.close()

	return None


# Функция заполняет таблицу с информацией об аренде книг в БД тестовыми данными
def fill_table_loans(db_name, loans_data):

	connection = sqlite3.connect(db_name)
	cursor = connection.cursor()

	for data in loans_data:
  		cursor.execute(
  			'INSERT INTO Loans (user_id, book_id, loan_start_date, loan_end_date) VALUES (?, ?, ?, ?)',
  			data)

	connection.commit()
	connection.close()

	return None


def main():
	DATABASE_NAME = 'library.db'
	create_db(DATABASE_NAME)
	create_table_users(DATABASE_NAME)
	create_table_books(DATABASE_NAME)
	create_table_loans(DATABASE_NAME)
	fill_table_users(DATABASE_NAME, db_test_data.users_data)
	fill_table_books(DATABASE_NAME, db_test_data.books_data)
	fill_table_loans(DATABASE_NAME, db_test_data.loans_data)


if __name__ == '__main__':
	main()