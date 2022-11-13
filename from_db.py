import os
from random import randint
import sqlite3 as db

def export_from_db (data, file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass
        
    connection = db.connect(file_name)
    cursor = connection.cursor()    

    cursor.execute('''
        CREATE TABLE person (
        id INTEGER,
        full_name TEXT,
        date_birth TEXT,
        telephone TEXT
        )
        ''').fetchall()


    for i in data[1::]:
        cursor.execute(f'''
            INSERT INTO person
            (id, full_name, date_birth, telephone)
            VALUES
            ("{i[0]}", "{i[1]}", "{i[2]}", "{i[3]}" );
            ''').fetchall()


    connection.commit()
    cursor.close()
    connection.close()

#----------------------------

def import_from_db (file_name):
    data = []        
    connection = db.connect(file_name)
    cursor = connection.cursor()   

#     temp = cursor.execute(f''' 
# SELECT column_name 
# FROM information_schema.columns 
# WHERE table_name = :a
#         ''').fetchall()
#     print(temp)

    # items = cursor.execute("SELECT * FROM person").fetchone()
    # for item in items:
    #     # print (items)
    #     data.append(item)

    cursor.execute("SELECT * FROM person")
    for i in cursor.execute("SELECT * FROM person"):
        temp = []
        for l in i:
            temp.append(l)
        data.append(temp)

    cursor.close()
    connection.close()

    return data
#----------------------------

if __name__ == '__main__':
    data = [['1', '2', '3', '4'], ['5', '6', '7', '8'], ['6','Жихарев АА','12.12.1988','+79997771548']]
    export_from_db (data, 'test.db')
    print (import_from_db('test.db'))
