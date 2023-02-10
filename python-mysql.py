import mysql.connector as connector

def create_database(dbname):
    query = f"CREATE DATABASE {dbname}"
    conn = connector.connect(host="localhost", user="root", password="")
    mycursor = conn.cursor()
    mycursor.execute(query)

def select_database():
    query = "SHOW DATABASES"
    conn = connector.connect(host="localhost", user="root", password="")
    mycursor = conn.cursor()
    mycursor.execute(query)
    result = mycursor.fetchall()
    for row in result:
        print(row)
    db = input("You Have above Listed Databases, Which Database you want to select write it :-")
    return db

def show_data(mycursor):
    result = mycursor.fetchall()
    for row in result:
        print(row)

def show_tables():
    query = "SHOW TABLES"
    mycursor.execute(query)
    show_data(mycursor)

def show_records():
    show_tables()
    table = input("You Have above Listed Tables Which table's Information you Want to See:-")
    query = f"SELECT * FROM {table}"
    # print(query)
    mycursor.execute(query)
    show_data(mycursor)

def create_table():
    tbname = input('What name you want to give your Table :-')
    columns = input('Write column name and Datatype as you want :- ')
    query = f"CREATE TABLE {tbname}({columns})"
    # print(query)
    mycursor.execute(query)
    if mycursor:
        print('Your table is Created Now you can go and see...')
    else:
        print('Something Went Wrong...')

def insert_record():
    show_tables()
    tbname = input('In Which table You Want to Enter Data Write it :- ')
    query = f"SHOW COLUMNS FROM {tbname}"
    mycursor.execute(query)
    result = mycursor.fetchall()
    columns = []
    collist = []
    for row in result:
        columns.append(list(row))
    z = 0
    for i in columns:
        collist.append(columns[z][0])
        z = z + 1
    data = []
    row = []
    no = int(input('How Many Row do you Want to Insert :-'))
    j = 0
    for x in range(0,no):
        for y in collist:
            row.append(input(f'Enter Value for {y}:'))
        data.append(tuple(row))
        row.clear()
    for k in data:
        query = f"INSERT INTO {tbname} VALUES{k}"
        mycursor.execute(query)
        conn.commit()

def update_record():
    show_tables()
    tblnm = input('In Which Table You want To Update :- ')
    query = f"SHOW COLUMNS FROM {tblnm}"
    mycursor.execute(query)
    result = mycursor.fetchall()
    columns = []
    collist = []
    for row in result:
        columns.append(list(row))
    j = 0
    for i in columns:
        collist.append(columns[j][0])
        j = j + 1

    query = f"SELECT * FROM {tblnm}"
    mycursor.execute(query)
    record = mycursor.fetchall()
    print(collist)
    for k in record:
        print(k)
    updatecol = input('You have above column And Data , in which column you Want to update :-')
    updatedata = input('What to Update :-')
    condition = input('Where you want to update Give id :- ')

    query = f"UPDATE {tblnm} SET {updatecol} = '{updatedata}' WHERE {collist[0]} = '{condition}'"
    mycursor.execute(query)
    conn.commit()

def delete_record():
    show_tables()
    tblnm = input('In Which Table You want To Delete :- ')
    query = f"SELECT * FROM {tblnm}"
    mycursor.execute(query)
    record = mycursor.fetchall()
    for k in record:
        print(k)

    query = f"SHOW COLUMNS FROM {tblnm}"
    mycursor.execute(query)
    result = mycursor.fetchall()
    columns = []
    collist = []
    for row in result:
        columns.append(list(row))
    j = 0
    for i in columns:
        collist.append(columns[j][0])
        j = j + 1
    id = input('Which record You Want to delete Give Id :- ')
    query = f"DELETE FROM {tblnm} WHERE {collist[0]} = '{id}'"
    mycursor.execute(query)
    conn.commit()

if __name__ == '__main__':
    n = input('You Want To Create New Database if yes then write y else n:- ')
    if n == 'y' or n == 'Y':
        dbname= input('What name you want to Give to your Database :-')
        create_database(dbname)
        conn = connector.connect(host="localhost", user="root", password="", database=dbname)
        mycursor = conn.cursor()
        print(f'Now you are in {dbname} Database')
    else:
        database = select_database()
        conn = connector.connect(host="localhost", user="root", password="",database = database)
        mycursor = conn.cursor()

    if mycursor:
        ch = 1
        while ch != 0:
            print('1:- Show Tables')
            print('2:- Show Records')
            print('3: Create Table')
            print('4: Insert Record')
            print('5:-Update Record')
            print('6: Delete Record')
            print('0:- Exit')
            ch = int(input("Enter Choice :- "))

            if ch == 1:
                show_tables()
            elif ch == 2:
                show_records()
            elif ch == 3:
                create_table()
            elif ch == 4:
                insert_record()
            elif ch == 5:
                update_record()
            elif ch == 6:
                delete_record()
            else:
                print("Invalid Choice")
    else:
        print("You write Wrong Database")
