# Chapter 12 - 2D Lists and Dictionaries
# Practice example code

# Challenge 096
'''
twod_list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
'''
# Challenge 097
'''
twod_list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
row_num = int(input("Enter a row number : "))
column_num = int(input("Enter a column number : "))
print(twod_list[row_num][column_num])
'''
# Challenge 098
'''
twod_list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
r_dis = int(input("Enter a row number you want to check : "))
print(twod_list[r_dis])
new_num = int(input("Enter a new value to that row : "))
twod_list[r_dis].append(new_num)
print(twod_list[r_dis])
'''
# Challenge 099
'''
twod_list = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
r_dis = int(input("Enter a row number you want to check : "))
print(twod_list[r_dis])
c_dis = int(input("Enter a column number you want to check : "))
print(twod_list[r_dis][c_dis])

ask = input("Do you want to change above  selected value (y/n)? ")
if ask == "y":
    new_value = int(input("Enter the value you want to update to : "))
    twod_list[r_dis][c_dis] = new_value
print(twod_list[r_dis])
'''
# Challenge 100
'''
twod_dic = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},
"Tom":{"N":4832,"S":6786,"E":4737,"W":3612},
"Anne":{"N":5239,"S":4802,"E":5820,"W":1859},
"Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}


print(twod_dic.values())
'''
# Challenge 101
'''
twod_dic = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},
"Tom":{"N":4832,"S":6786,"E":4737,"W":3612},
"Anne":{"N":5239,"S":4802,"E":5820,"W":1859},
"Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}

name = input("Enter a name you want to check : ")
region = input("Enter a region you want to check under above selected name : ")
print(twod_dic[name][region])

ask = input("Do you want to update data on the 2D dictionary (y/n)? ")
if ask == "y":
    ask_name = input("Enter a name you want to update : ")
    ask_region = input("Enter a region you want to update under above selected name : ")
    update_num = int(input("Enter the update number : "))
    twod_dic[ask_name][ask_region] = update_num
print(twod_dic[ask_name])
'''
# Challenge 102
'''
my_2dlist = {}

for i in range(0,4):
    name = input("Enter a name : ")
    age = int(input("Enter the age : "))
    size = int(input("Enter the shoe size : "))
    my_2dlist[name] = {"Age":age,"Shoe size": size}

ask_name = input("Enter the name you want to check : ")
print(my_2dlist[ask_name])
print(my_2dlist)
'''
# Challenge 103
'''
my_2dlist = {}

for i in range(0,4):
    name = input("Enter a name : ")
    age = int(input("Enter the age : "))
    size = int(input("Enter the shoe size : "))
    my_2dlist[name] = {"Age":age,"Shoe size": size}

for x in my_2dlist:
    print(x,"Age",my_2dlist[x]["Age"])


twod_dic = {"Kevin":{"Age":18,"Shoe size":9},
"Mei":{"Age":20,"Shoe size":7},
"Lucy":{"Age":30,"Shoe size":6},
"Peter":{"Age":33,"Shoe size":8}}

for i in twod_dic:
    print(i,twod_dic[i]["Age"])
'''
# Challenge 104
'''
twod_dic = {}
for i in range(0,4):
    name = input("Enter a name : ")
    age = int(input("Enter the age : "))
    size = int(input("Enter the shoe size : "))
    twod_dic[name]={"Age":age,"Shoe size":size}

ask_name = input("Enter the name you want to delete drom the data : ")
del twod_dic[ask_name]

for name in twod_dic:
    print(name,twod_dic[name]["Age"],twod_dic[name]["Shoe size"])
'''

twod_dic = {"Kevin":{"Age":18,"Shoe size":9},
"Mei":{"Age":20,"Shoe size":7},
"Lucy":{"Age":30,"Shoe size":6},
"Peter":{"Age":33,"Shoe size":8}}

for i in twod_dic:
    print(i,twod_dic[i])















    
