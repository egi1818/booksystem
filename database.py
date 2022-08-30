# import sqlite3
import psycopg2
from psycopg2 import Error

try:
	connection = psycopg2.connect(user="lnunmydamiypgu",
									password="c15d7dfc4fa15bb17ab4411cff3adac1e012d86a4fdf2fa4e2e01d769b1c98de",
									host="ec2-35-168-122-84.compute-1.amazonaws.com",
									port="5432",
									database="d8slr01vp3bhig")
	#database instance
	# conn = sqlite3.connect('database.db')
	cursor = connection.cursor()
	#tables
	cursor.execute('''CREATE TABLE users 
			(userId SERIAL PRIMARY KEY, 
			password TEXT,
			email TEXT,
			name TEXT,
			userType TEXT,
			createDate TEXT
			)''')
	connection.commit()

	cursor.execute('''CREATE TABLE books
			(bookId SERIAL PRIMARY KEY,
			userId INTEGER,
			bookName TEXT,
			authorName TEXT,
			price REAL,
			description TEXT,
			image TEXT,
			createDate TEXT,
			updateDate TEXT,
			status INTEGER DEFAULT 1,
			FOREIGN KEY(userId) REFERENCES users(userId)
			)''')
	connection.commit()

	cursor.execute('''CREATE TABLE comment 
			(commentId SERIAL PRIMARY KEY,
			userId INTEGER,
			bookId INTEGER,
	      ratings INTEGER,
			message TEXT,
			createDate TEXT,
			FOREIGN KEY(userId) REFERENCES users(userId),
			FOREIGN KEY(bookId) REFERENCES books(bookId)
			)''')
	connection.commit()

	print("Table created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")