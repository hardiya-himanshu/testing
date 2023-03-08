# PRINTING

#this is comment
'''this is multiline
dfdfddg
comment'''
# import os
# print("Hello World")

# COMMENT

# practice 1
# print('''
# wwew
# wee
# we
# rer
# ''')

# AUDIO IN PYTHON

# from playsound import playsound
# playsound('C:\\Users\\RYZEN\\Downloads\\song.mp3')

# STRINGS

# name='himanshu'
# print(name[0:5])
# print(name[-8:-1])
# print(name[:])
# print(name[1:7:2])


# print(len(name))
# print(name.endswith("u"))
# print(name.count("h"))
# print(name.capitalize())
# print(name.find("s"))
# print(name.replace("h","b"))

# ESCAPE SEQUENCE

# \t for spacing a tab, \n for new line, \\ for backslash(\), \' for single quote.

# name = "This is himanshu.\nNot only himanshu it's Himanshu Hardiya."
# print(name)


# name = "himanshu  hardiya"
# print(name.replace("  ", " "))

# letter = "Dear Hardiya, This Python Course is nice. Thanks!"
# print(letter)
# letter = "Dear Hardiya,\n\tThis Python Course is nice.\nThanks!"
# print(letter)


# LIST
# list = [1, 5, 7, 2, 96, 3]
# append(value) remove(value) pop(index) insert(index,value) sort reverse
# list.remove(2)
# print(list)

# TUPLE - it is created using ()

# t = (1, 2, 5, 7, 8, 1, 3)
# print(t)

# print(t.count(1))
# print(t.index(8))

# t1=() null or empty tuple
# t2=(2,)


# first = input("Enter name of first fruit : ")
# second = input("Enter name of second fruit : ")
# third = input("Enter name of third fruit : ")
# fourth = input("Enter name of fourth fruit : ")
# fifth = input("Enter name of fifth fruit : ")
# sixth = input("Enter name of sixth fruit : ")
# seventh = input("Enter name of seventh fruit : ")

# fruitlist = [first, second, third, fourth, fifth, sixth, seventh]

# print(fruitlist)


# s1 = int(input())
# s2 = int(input())
# s3 = int(input())
# s4 = int(input())
# s5 = int(input())
# s6 = int(input())

# marks = [s1, s2, s3, s4, s5, s6]
# marks.sort()
# print(marks)


# a=(7,0,8,0,0,9)
# print(a.count(0))

# DICTIONARY

# dictionary = {
#     "himanshu": "Name",
#     "hardiya": "Surname"
# }
# print(dictionary["hardiya"]) # to print the value of a key in that particular dictionary

# properties of dictionary

# print(list(dictionary.keys()))  # to print keys
# print(list(dictionary.values()))  # to print values
# print(list(dictionary.items()))

# update_dictionary = {'yogesh': 'middle_name'}

# dictionary.update(update_dictionary)
# print(list(dictionary))

# print(dictionary.get("himanshu"))

# SETS

# x = {1, 2, 3, 4, 5,1,2}  # this x is a set : collection of non-repitative elements

# print(x)
# print(type(x))

# a = {}  //# not an empty set
# a = set()
# a.add(1)  # adding 1 into a set a.
# print(a)
# print(type(a))  # it is an dictionary not an empty set


# i1 = int(input())
# i2 = int(input())
# i3 = int(input())
# i4 = int(input())
# i5 = int(input())
# i6 = int(input())
# i7 = int(input())
# i8 = int(input())

# a = {i1, i2, i3, i4, i5, i6, i7, i8}

# print(a)


# WHILE LOOP


# i = 1
# while i <= 50:
#     print(i)
#     i += 1  # i=i+1  or i+=1


# list = ["ram", "shyam", "hari", "prakash", "vijay", "abhinav", "raj"]
# i = 0
# while i < len(list):
#     print(list[i])
#     i = i+1


# num = int(input("Enter any no. : "))

# for i in range(1, 11):
#     # print(str(num)+" x "+str(i)+" = "+str(num*i))
#     # this can be done by fstring method.
#     print(f"{num} x {i} = {num*i}")


# num = int(input("Enter any no. : "))
# i = 1
# while i < 11:
#     print(f"{num} x {i} = {num*i}")
#     i = i+1


# n = int(input("Enter any no. : "))


# sum = 0
# # for i in range(2, num):
# #     if num % i == 0:
# #         print("No. is Not Prime")
# #         break
# #     else:
# #         print("No. is Prime")
# #         break


# for i in range(1, num+1):
#     sum = sum+i
# print(sum)


# fact = 1
# for i in range(num, 0, -1):
#     fact = fact*i
# print(fact)


# for i in range(1, 4):

#     print("* "*i)

# n = 1
# for i in range(1, 4):
#     print("* "*(2*n+i))
#     print("* "*(n), end="")
#     print("  "*(n), end="")
#     print("* "*(n), end="")


# def add(x,y):
#     return x+y
# print(add(9,5))

# def facto(n):
#     fact=1
#     for i in range(n):
#         fact=fact*(i+1)
#     print(fact)

# facto(7)


# def cel_to_fhrt(n):
#     fhrt=(n*(9/5)+32)
#     return fhrt

# print("fahrenheit : ", cel_to_fhrt(40))


# def star(n):
#     for i in range(n):
#         print("* "*(n-i))
# star(7)


# def inch_to_cntm(n):
#     cntm=2.54*n
#     return cntm

# print(inch_to_cntm(12))

# def table(n):
#     for i in range(1, 11):
#         print(n, " x ", i, " = ", (n*i))


# table(7)

# import random


# def game(a, b):
#     if a == b:
#         return None

#     elif a == 's':
#         if b == 'w':
#             return True
#         else:
#             return False
#     elif a == 'w':
#         if b == 's':
#             return False
#         else:
#             return True
#     elif a == 'g':
#         if b == 'w':
#             return False
#         else:
#             return True


# def play():
#     player = input("Enter any from Snake(s) / Water(w) / Gun(g) : ")

#     computer = random.randint(0, 2)

#     if computer == 0:
#         computer = 's'
#         ff = 'Snake'
#     elif computer == 1:
#         computer = 'w'
#         ff = 'Water'
#     else:
#         computer = 'g'
#         ff = 'Gun'

#     print("Computer Select : ", computer, "(", ff, ")")

#     result = game(player, computer)

#     if result:
#         print("\nCongrats! You Win.\n")

#         ans = input("Do You Want to Play Again(y/n) : ")
#         print("\n")
#         if ans == 'y':
#             play()
#         else:
#             pass

#     elif result == None:
#         print("\nOops! The Match is Tie.\n")

#         ans = input("Do You Want to Play Again(y/n) : ")
#         print("\n")
#         if ans == 'y':
#             play()
#         else:
#             pass

#     else:
#         print("\nAlas! You Lost.\n")
#         ans = input("Do You Want to Play Again(y/n) : ")
#         print("\n")
#         if ans == 'y':
#             play()
#         else:
#             pass


# play()


# files


# f = open("sample.txt", "r")
# data = f.read()
# print(data)
# f.close()


# write mode:

# f = open("sample2.txt", "w")
# f.write("My age is 21.")
# f.close()


# f = open('poems.txt', 'r')
# data = f.read()
# if 'twinlk' in data:
#     print("True")
# else:
#     print("False")
# f.close()


# def game():
#     s = int(input("Enter Your Score : "))
#     return s


# def read():
#     with open('Highscore.txt', 'r') as f1:
#         hs=int(f1.read())
#         return hs

# def update():
#     with open('Highscore.txt', 'w') as f:
#         f.write(score)


# score = game()
# highscore=read()
# if highscore<score:
#     score=str(score)
#     update()
#     print("Highscore Updated")
# else:
#     print("You Score Less Than Highscore")

# with open("speech.txt", "r") as f:
#     data = f.read()


# if "donkey" in data:
#     data2 = data.replace("donkey", "######")
#     with open("speech.txt", "w") as f1:
#         f1.write(data2)

# OOPS

class Number:
    def sum(self):
        return self.a+ self.b

num=Number()
num.a=10
num.b=9
s=num.sum()
print(s)