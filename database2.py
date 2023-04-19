import sqlite3

# N1
conn = sqlite3.connect("customers.sqlite")
cursor = conn.cursor()
# N2
result = cursor.execute("SELECT * FROM users")
all_rows = cursor.fetchall()
for row in all_rows:
    print("username:", row[1], "phonenumber:", row[5])
# N3
result1 = cursor.execute("SELECT * FROM users WHERE age > 25")
All_rows = cursor.fetchall()
for Row in All_rows:
    print("firstname:", Row[2], "lastname:", Row[3], "age:", Row[4])
age = 25

Result = cursor.execute("SELECT * FROM users WHERE age > :age_condition", {"age_condition": age})
all_rows1 = cursor.fetchall()
for Row in all_rows1:
    print("firstname:", Row[2], "lastname:", Row[3], "age:", Row[4])
# N4
ResulT = cursor.execute("SELECT * FROM users WHERE age BETWEEN 10 AND 25")
for row in ResulT:
    print(row)
# N5
ResuLT = cursor.execute("SELECT * FROM users WHERE age <> 20")
ALL_rows = cursor.fetchall()
for row in ALL_rows:
    print("firstname: ", row[2], " lastname: ", row[3])
# N6
select_result = cursor.execute("SELECT count(user_id) as id_count FROM users")
for row in select_result:
    print(row)
# N7
resulT = cursor.execute("SELECT * FROM users order by age desc")
for row in resulT:
    print(row)
# N8
unique_names = cursor.execute("SELECT DISTINCT firstname FROM users order by firstname")
for row in unique_names:
    print(row)
# N9
cursor.execute("UPDATE users SET firstname = 'tarieli' WHERE age = 20")
conn.commit()
# N10
cursor.execute("UPDATE users SET age = 15 WHERE age > 30")
conn.commit()
# N11
cursor.execute("DELETE FROM users WHERE user_id = 5")
conn.commit()
# N12
cursor.execute("DELETE FROM users WHERE firstname LIKE 'ა%';")
conn.commit()
# N13
conn.close()
