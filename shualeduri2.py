import sqlite3

import json
conn = sqlite3.connect("survey 2.sqlite")
cursor = conn.cursor()
select_result = cursor.execute("SELECT count(ID) as id_count FROM students WHERE SelfStudyHour < 2")
for row in select_result:
    print(row)


def function(Socialmediaplatform, age):
    result = cursor.execute(
        "SELECT count(ID) as som_count FROM students WHERE SocialMediaPlatform = :Socialmedia AND Age = :age",
        {"Socialmedia": Socialmediaplatform, "age": age})
    for row1 in result:
        print(row1)


function("Youtube", 20)
# cursor.execute("""INSERT INTO students(Device, age, OnlineClassTime, FitnessTime, Sleep, SocialMedia,
# SocialMediaPlatform) VALUES("ნიკოლოზ მებონია", 15, 4, 2, 8, 2, "Youtube")""")
# conn.commit()
# cursor.execute("UPDATE students SET device = 'ნიკოლოზი' WHERE age > 19")
# conn.commit()
conn.close()
file_object = open("sample.json", "r+")
content = file_object.read()
content_loads = json.loads(content)
print(content_loads)
eyecolor = content_loads["person"]["eyeColor"]
print(eyecolor)
friends = content_loads["person"]["friends"]
for name in range(len(friends)):
    list_1 = []
    list_1.append(friends[name]["name"])
    print(list_1)
key = input("key: ")
person = content_loads["person"]
print(person[key])

file_object.close()