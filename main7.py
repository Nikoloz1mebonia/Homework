import sqlite3


# N1
conn = sqlite3.connect("books_db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE books_table
(book_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(50),
author VARCHAR(40),
release_year INT,
price INT);
""")
cursor.execute("""
INSERT INTO books_table(title, author, release_year, price) VALUES('ვეფხისტყაოსანი', ' შოთა რუსთაველი', 1197, 85)""");
conn.commit()
book_list = [
    ("შვილის ნუკრის ნაამბობი", "ვაჟა ფშაველა", 1896, 45),
    ("რაღაც წიგნი", "ნიკოლოზ მებონია", 2023, 112),
    ("კიდევ წიგნი", "ნინი კვინიკაძე", 1800, 111),
    ("კიდევ წიგნი", "ანასტასია მაისურაძე", 1799, 111)
]
cursor.executemany('INSERT INTO books_table(title, author, release_year, price) VALUES(?, ?, ?, ?)', book_list)
conn.commit()
conn.close()
# N2
conn1 = sqlite3.connect("titanic")
cursor1 = conn1.cursor()
cursor1.execute("""CREATE TABLE titanic_table
(passenger_id INTEGER PRIMARY KEY AUTOINCREMENT,
passenger_name VARCHAR(35),
age INT,
sex VARCHAR(6),
ticket INT,
cabin INT);
""")
name = input("insert a name: ")
age = int(input("insert age: "))
sex = input("gender: ")
ticket = int(input("ticket number: "))
cabin = int(input("cabin: "))
cursor1.execute('INSERT INTO titanic_table(passenger_name, age, sex, ticket, cabin) VALUES(?, ?, ?, ?, ?)', (name, age,
                                                                                                             sex,
                                                                                                             ticket,
                                                                                                             cabin));
conn1.commit()
titanic_list = []
for i in range(1, 4):
    name1 = input("insert name: ")
    age1 =int(input("insert age: "))
    sex1 = input("gender: ")
    ticket1 = int(input("ticket: "))
    cabin1 = int(input("cabin: "))
    sum = (name1, age1, sex1, ticket1, cabin1)
    titanic_list.append(sum)

cursor1.executemany('INSERT INTO titanic_table(passenger_name, age, sex, ticket, cabin) VALUES(?, ?, ?, ?, ?)',
                    titanic_list)
conn1.commit()
conn1.close()
# N3
class Movie:
    def __init__(self, title, genre, year, imdb):
        self.title = title
        self.genre = genre
        self.year = year
        self.imdb = imdb

    def __str__(self):
        return f"title: {self.title}, genre: {self.genre}, year: {self.year}, imdb: {self.imdb}"


conn2 = sqlite3.connect("movies")
cursor2 =  conn2.cursor()
cursor2.execute("""CREATE TABLE movies_table
(movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(35),
genre VARCHAR(40),
year INT,
imdb VARCHAR(300));
""")
movie1 = Movie("interstellar", "futuristic", 2014, "review")
cursor2.execute('INSERT INTO movies_table(title, genre, year, imdb) VALUES(?, ?, ?, ?)', (movie1.title, movie1.genre,
                                                                                          movie1.year, movie1.imdb));
conn2.commit()
movie2 = Movie("induri", "drama", 2016, "review")
movie3 = Movie("turquli", "drama", 2020, "review")
movie_list = [
    (movie2.title, movie2.genre, movie2.year, movie2.imdb),
    (movie3.title, movie3.genre, movie3.year, movie3.imdb)
]
cursor2.executemany('INSERT INTO movies_table(title, genre, year, imdb) VALUES(?, ?, ?, ?)', movie_list)
conn2.commit()
conn2.close()
print(movie1)