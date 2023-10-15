"""Создать таблицу со студентами в БД,
Создать таблицу аудиторий в БД,
Сделать связь таблиц"""

import psycopg2

conn = psycopg2.connect(
    dbname='homework',
    user='postgres',
    password='qwerty',
    host='127.0.0.1'
)

conn.autocommit = True

with conn.cursor() as cursor:
    cursor.execute(
        "CREATE TABLE room (id serial PRIMARY KEY, "
        "number TEXT NOT NULL, floor INT NOT NULL);"
    )
    print(f'[INFO] CREATE TABLE successfully')

with conn.cursor() as cursor:
    cursor.execute(
        "CREATE TABLE student(id serial PRIMARY KEY, "
        "name TEXT NOT NULL, age INT NOT NULL, "
        "fk_conn INT REFERENCES room(id));"
    )
    print(f'[INFO] CREATE TABLE successfully')

with conn.cursor() as cursor:
    cursor.execute(
        "INSERT INTO room(number, floor) VALUES (100, 1);"
        "INSERT INTO room(number, floor) VALUES (200, 2);"
    )
    print(f'[INFO] CREATE TABLE successfully')

with conn.cursor() as cursor:
    cursor.execute(
        "INSERT INTO student(name, age, fk_conn) VALUES ('Oleg', 25, 1);"
        "INSERT INTO student(name, age, fk_conn) VALUES ('IGOR', 24, 1);"
        "INSERT INTO student(name, age, fk_conn) VALUES ('Vlad', 25, 2);"
        "INSERT INTO student(name, age, fk_conn) VALUES ('GLEB', 22, 2);"

    )
    print(f'[INFO] CREATE TABLE successfully')

with conn.cursor() as cursor:
    cursor.execute("SELECT student.name, room.number FROM student, "
                   "room WHERE room.id=student.fk_conn;"
                   )

    print(f'{cursor.fetchall()}')


conn.close()

""" СОздать БД с двумя таблицами, соединить их JOINOM, подключить функции к запросам """
with conn.cursor() as cursor:
    cursor.execute('SELECT student.name, room.number FROM student INNER JOIN room ON student.fk_conn = room.id;'
                   )
    print(f'{cursor.fetchall()}')


with conn.cursor() as cursor:
    cursor.execute("SELECT AVG(age) FROM student;"
                   )
    print(f'{cursor.fetchone()}')

conn.close()