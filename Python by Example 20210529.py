from tkinter import*
import sqlite3

with sqlite3.connect("TestScores.db") as db:
    cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student_test(
Name text PRIMARY KEY,
Grade integer NOT NULL);""")

def add_sql():
    names = name_entry.get()
    grades = int(grade_entry.get())
    cursor.execute("""INSERT INTO student_test(Name,Grade)
VALUES(?,?)""",(names,grades))
    db.commit()
    name_entry.delete(0,END)
    grade_entry.delete(0,END)
    
def clear_window():
    name_entry.delete(0,END)
    grade_entry.delete(0,END)
    name_entry.focus()


window = Tk()
window.geometry("600x400")
window.title("TestScores")

label01 = Label(text="Enter student's name : ")
label01.place(x=30,y=60,width=150,height=30)

label02 = Label(text="Enter student's grade :")
label02.place(x=30,y=120,width=150,height=30)

name_entry = Entry(text="")
name_entry.place(x=210,y=60,width=250,height=30)
name_entry["justify"]="center"

grade_entry = Entry(text="")
grade_entry.place(x=210,y=120,width=250,height=30)
grade_entry["justify"]="center"

add_button = Button(text="Add",command=add_sql)
add_button.place(x=210,y=180,width=80,height=30)

clear_button = Button(text="Clear",command=clear_window)
clear_button.place(x=330,y=180,width=80,height=30)



window.mainloop()
