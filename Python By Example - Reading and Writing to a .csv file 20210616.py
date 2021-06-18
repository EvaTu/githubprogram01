# Chapter 14 - Reading and Writing to a .csv file
# Practice example code

# Challenge 111
'''
import csv

file = open("Book.csv","w")
file.write(str("To Kill A Mockingbird, Harper Lee, 1960\n"))
file.write(str("A Brief History of Time, Stephen Hawking, 1988\n"))
file.write(str("The Great Gatsby, F. Scott Fitzgerald, 1922\n"))
file.write(str("The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"))
file.write(str("Pride and Prejudice, Jane Austen, 1813\n"))

file.close()
'''
# Challenge 112
'''
import csv

file = open("Books.csv","a")
book_name = input("Enter a book name : ")
author = input("Enter the author name : ")
year = input("Enter the book publish year : ")
new_data = str(book_name+","+author+","+year+"\n")
file.write(new_data)
file.close()

file = open("Books.csv","r")
for row in file:
    print(row)
file.close()


file = open("Books.csv","r")
reader = csv.reader(file)
row = list(reader)
print(row)
file.close()
'''
'''
file = open("Subject.txt","r")
a = file.read()
print(a)
'''
# Challenge 113
'''
import csv

ask = int(input("How many new data you want to add to .csv file : "))
file = open("Books.csv","a")
for i in range(0,ask):
    book_name = input("Enter a book name : ")
    author = input("Enter the author name : ")
    year = input("Enter the published year : ")
    new_data = str(book_name+", "+author+", "+year+"\n")
    file.write(new_data)
file.close()
print()
file = open("Books.csv","r")
search = input("Enter the name of the author you would like to check : ")
reader = csv.reader(file)
for row in file:
    if search in str(row):
        print(row)
file.close()
'''
# Challenge 114
'''
import csv

num1 = int(input("Enter a start search published year : "))
num2 = int(input("Enter a end search published year : "))
file = list(csv.reader(open("Books.csv","r")))
temp = []
for i in file:
    temp.append(i)

x = 0
for row in temp:
    if int(temp[x][2])>=num1 and int(temp[x][2])<=num2:
        print(temp[x])
    x = x + 1
'''
# Challenge 115
'''
import csv

file = open("Books.csv","r")
x = 0
for row in file:
    print("No.",x," ",row)
    x = x + 1
file.close()
'''
# Challenge 116
'''
import csv

file = list(csv.reader(open("Books.csv")))
temp = []
for i in file:
    temp.append(i)
    print(i)

ask = int(input("Enter the row number you want to delete : "))
del temp[ask]

change_row = int(input("Enter the row you want to change : "))
change_item = int(input("Enter the item number under above row number : "))
info = input("Enter the data you want to update : ")
temp[change_row][change_item] = info

x = 0
file = open("Books.csv","w")
for row in temp:
    update = temp[x][0]+", "+temp[x][1]+", "+temp[x][2]+"\n"
    file.write(update)
    x = x + 1
file.close()
'''
# Challenge 117
'''
import random
import csv

file = open("Fun Math.csv","a")

name = input("Enter your name : ")
num1 = random.randint(1,100)
num2 = random.randint(1,100)
math_q = str(num1)+" + "+str(num2)+" = "
print(math_q)
ans = int(input("Your answer is : "))
check = num1 + num2
score = 0
if ans == check :
    score = score + 1

new_data = name+", "+math_q+", "+str(ans)+", "+str(score)+"\n"
file.write(str(new_data))

file.close()
'''
    























