# challenge 139
'''
import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
ID integer PRIMARY KEY,
First_Name text NOT NULL,
Surname text NOT NULL,
Phone_Number blob NOT NULL);""")

for i in range(0,3):
    newID = input("Enter a number : ")
    newFirst_Name = input("Enter First Name : ")    
    newSurname = input("Enter Surname : ")
    newPhone_Number = input("Enter Phone Number : ")
    cursor.execute("""INSERT INTO Names(ID,First_Name,Surname,Phone_Number)
VALUES(?,?,?,?)""",(newID,newFirst_Name,newSurname,newPhone_Number))

db.commit()

cursor.execute("UPDATE Names SET Phone_Number = '01954 295773' WHERE ID = 2")
db.commit()
'''

# challenge 140
'''
import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()
    
selection = input("""Main Menu
1) View phone book
2) Add to phone book
3) Search for surname
4) Delete person from book
5) Quit

Enter your selection :  """)

print("\n")

if selection == "1":
    cursor.execute("SELECT * FROM Names")
    for i in cursor.fetchall():
        print(i)
elif selection == "2":
    newID = input("Enter a number : ")
    newFirst_Name = input("Enter First Name : ")    
    newSurname = input("Enter Surname : ")
    newPhone_Number = input("Enter Phone Number : ")
    cursor.execute("""INSERT INTO Names(ID,First_Name,Surname,Phone_Number)
VALUES(?,?,?,?)""",(newID,newFirst_Name,newSurname,newPhone_Number))
    db.commit()
elif selection == "3":
    whichSurname = input("Enter Surname : ")
    cursor.execute("SELECT * FROM Names WHERE Surname = ?",[whichSurname])
    print(cursor.fetchall())
elif selection == "4":
    delID = int(input("Enter an ID : "))
    cursor.execute("DELETE FROM Names WHERE ID = ?",[delID])
    db.commit()
elif selection == "5":
    db.close()
    
else:
    print("You entered an invalid info")

'''

# challenge 141
'''
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
Name text PRIMARY KEY,
Place_of_Birth text NOT NULL);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
ID integer PRIMARY KEY,
Title text NOT NULL,
Author text NOT NULL,
Date_Published integer NOT NULL);""")
# data for Authors Table
cursor.execute("""INSERT INTO Authors(Name,Place_of_Birth)
VALUES("Agatha Chritie","Torquay")""")
cursor.execute("""INSERT INTO Authors(Name,Place_of_Birth)
VALUES("Cecelia Ahern","Dublin")""")
cursor.execute("""INSERT INTO Authors(Name,Place_of_Birth)
VALUES("J.K. Rowling","Bristol")""")
cursor.execute("""INSERT INTO Authors(Name,Place_of_Birth)
VALUES("Oscar Wilde","Dublin")""")
# data for Books Table
cursor.execute("""INSERT INTO Books(ID,Title,Author,Date_Published)
VALUES("1","De Profundis","Oscar Wilde","1905")""")
cursor.execute("""INSERT INTO Books(ID,Title,Author,Date_Published)
VALUES("2","Harry Potter and the chamber of secrets","J.K. Rowling","1998")""")
cursor.execute("""INSERT INTO Books(ID,Title,Author,Date_Published)
VALUES("3","Harry Potter and the prisoner of Azkaban","J.K. Rowling","1999")""")
cursor.execute("""INSERT INTO Books(ID,Title,Author,Date_Published)
VALUES("4","Lyrebird","Cecelia Ahern","2017")""")
cursor.execute("""INSERT INTO Books(ID,Title,Author,Date_Published)
VALUES("5","Murder on the Orient Express","Agatha Christie","1934")""")
cursor.execute("""INSERT INTO Books(ID,Title,Author,Date_Published)
VALUES("6","Perfect","Cecelia Ahern","2017")""")
cursor.execute("""INSERT INTO Books(ID,Title,Author,Date_Published)
VALUES("7","The marble collector","Cecelia Ahern","2016")""")
cursor.execute("""INSERT INTO Books(ID,Title,Author,Date_Published)
VALUES("8","The murder on the links","Agatha Christie","1923")""")
cursor.execute("""INSERT INTO Books(ID,Title,Author,Date_Published)
VALUES("9","The picture of Dorian Gray","Oscar Wilde","1890")""")
cursor.execute("""INSERT INTO Books(ID,Title,Author,Date_Published)
VALUES("10","The secret adversary","Agatha Christie","1921")""")
cursor.execute("""INSERT INTO Books(ID,Title,Author,Date_Published)
VALUES("11","The seven dials mystery","Agatha Christie","1929")""")
cursor.execute("""INSERT INTO Books(ID,Title,Author,Date_Published)
VALUES("12","The year I met you","Cecelia Ahern","2014")""")

db.commit()
db.close()
'''
# challenge 142
'''
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Authors")
for i in cursor.fetchall():
    print(i)

sel_bp = input("Enter birth place of an author : ")
cursor.execute("""SELECT Books.Title,Books.Author,Books.Date_Published
FROM Books,Authors WHERE Books.Author = Authors.Name
AND Place_of_Birth = ?""",[sel_bp])
for i in cursor.fetchall():
    print(i)

"""
cursor.execute("UPDATE Authors SET Name='Agatha Christie' WHERE Place_of_Birth='Torquay'")
db.commit()
"""
'''

# challenge 143
'''
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

year = input("Enter a year : ")

cursor.execute("""SELECT Books.Title,Books.Author,Books.Date_Published
FROM Books WHERE Date_Published>? ORDER BY Date_Published""",[year])
for i in cursor.fetchall():
    print(i)
'''

# challenge 144
'''
import sqlite3
with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()
file = open("BookInfo.text","w")

cursor.execute("SELECT Name FROM Authors")
for i in cursor.fetchall():
    print(i)

e_author = input("Enter an author : ")

cursor.execute("SELECT * FROM Books WHERE Author = ?",[e_author])
for i in cursor.fetchall():
    new_data = str(i[0])+" - "+str(i[1])+" - "+str(i[2])+" - "+str(i[3])+"\n"
    file.write(new_data)
file.close() 
db.close()
'''






