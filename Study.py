# birth_year= input('Birth year: ')
# print(type(birth_year))

# age= 2019- int(birth_year)
# print(type(age))
# print(age)


# Weight_lbs=float(input('What is your weight in pounds?: '))
# weight_kg= float(Weight_lbs)*0.45
# final_weight= (weight_kg)
# print(final_weight)

# course='Python for beginners'
# print(course[0:])
# another=course[:]
# print(another)

# name="Bernardine"
# print(name[1:-1])

# #Formatted strings
# first='Bernardine'
# last='Adusei'
# msg=f'{first} [{last}] is a coder'
# print(msg)
# course='Python for Beginners'
# print(course)
# print(len(course))
# print(course.upper())
# print(course.lower())

# print(course.find('Beginners'))
# print(course.replace('Beginners','Absolute Beginners'))
# print('Python' in course)

# #Arithmetic Operations
# print(10/3)

# print(10**3)
# x=10
# # x=x+3
# x+=3

# #Operator Precedence{Like BODMAS}
# x= 10 + 3 * 2
# print(x)

# #Math functions
# import math
# x=2.9
# print(math.ceil(2.9))
# print(math.floor(2.9))
# print(round(x))
# print(abs(-2.9))

# #If Statement
# is_hot=False
# is_cold=False
# if is_hot:
#     print("It's a hot day")
#     print("Drink Plenty of Water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:    
#    print("It's a lovely day!")

# print("Enjoy your day!")

# house_price=1000000
# has_good_credit=True
# has_bad_credit= False

# if has_good_credit:
#     print('They need to put down: ')
#     print(float(float(10/100)*house_price))

# elif has_bad_credit:
#         print(float(float(20/100)*house_price))

# #Logical Operators
# has_high_income= True
# has_good_credit=False
# has_criminal_record=False
# # if has_high_income or has_good_credit:
# #     print('Eligible to take a loan')
# if has_good_credit and not has_criminal_record:
#      print('Eligible to take a loan')
# else:
#      print ('Not eligible for a loan')

# #Comparison Operators
# temperature=30
# if temperature==30:
#     print("It's a hot day!")
# else:
#     print("It's not a hot day")
  
# name="Bernardine Adusei-Okrah"

# if len(name)<3:
#     print("Name must be at least 3 characters long")
# elif len(name)>50:
#     print("Name cam be a maximum of 50 characters")
# else:
#     print("Name looks good!")

# weight=int(input('Weight: '))
# unit=input('(L)bs or (K)g: ')
# if unit.upper == "L":
#     converted= weight*0.45
#     print(f'You are {converted} kilos')
# else:
#     converted=weight/0.45
#     print(f'You are {converted} pounds')

# #While loops
# #while condition:
# i=1
# while i<5:
#     print('*' * i)
#     i=i+1
# print("Done!")

# #Guessing Game
# secret_number=9
# guess_count=0
# guess_limit=3
# while guess_count< guess_limit:
#     guess=int(input("Guess: "))
#     guess_count +=1
#     if guess==secret_number:
#      print('You won!')
#      break
# else:
#        print('Sorry you failed!')

# #For loops
# for item in "Python":
#     print(item)
# for item in ["Bernardine","Adusei","Kobby"]:
#     print(item)

# prices=[10,20,30]
# total_cost=prices[0]+prices[1]+prices[2]
# for item in prices:
#     print(f'Total cost is ${total_cost}')
#     break
# total= 0
# for price in prices:
#  total+=price
# print(f'Total: ${total}')

# #Nested Loops
# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

# #Lists
# names=['John','James','Mary']
# print(names[:])

# Numbers=[1,2,3,4,5,6,7,8]
# max= Numbers[0]
# for number in Numbers:
#     if number> max:
#         max=number
# print(max)

# # Tuples
# # Cannot be duplicated and all-->Most methods cannot be used on them

# Unpacking
# coordinates=(1,2,3)
# # x= coordinates[0]
# # y= coordintaes[1]
# # z= coordinates[2]
# x,y,z= coordinates
# print(x)
# print(y)
# print(z)

# # Dictionaries 
# # They are for storing values that come as key value pairs
# # Each word is listed once in a dictionary
# Customer={
#     "name":"Bernardine Okrah",
#     "age":30,
#     "is_verififed":True
# }
# Customer["name"]="Kwabena Adusei"
# # print(Customer["name"])
# print(Customer.get("name"))
# # print(Customer.get("Birthdate","April 27, 2004"))
# Customer["Birthdate"]="January 1,2024"
# print(Customer.get("Birthdate"))

# phone=input("Phone: ")
# digits_mapping={
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four"
# }
# output = ""
# for ch in phone:
#    output += digits_mapping.get(ch,"!") + " "
   
# print(output)

# # Functions, Parameters, Arguments
# # A container for a few lines of code that perform specific tasks
# # Parameters are place holders that we define in our function for receiving information
# # Arguments are the actual pieces of information supplied to the functions
# def greet_user(first_name,last_name):
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard!')


# print("Start")
# greet_user("Bernardine","Adusei-Okrah")

# print('Finish')

# # Keyword Arguments-->Parameter name followed by its value
# # Keyword arguments should always come after positional arguments

# # Return Statement
# # By default all funtcions return the value None
# def square(number):
#    return number*number
# result=square(8)
# print(result)

# # Exception HAndling
# try except-->To handle errors
# try:
#     age=int(input('Age: '))
#     income=20000
#     risk=income/age
#     print (age)
# except ZeroDivisionError:
#     print('Age cannot be zero')
# except ValueError:
#     print("Invalid Value")

# #Comments[For communication]
# print('Sky is blue')

# # Classes
# # The class defines the blue print or the template for creating objects
# # Capitalize first letter of every word when naming classes
# # object is an insatnce of a class
# Numbers=[1,2,3,4]
# class Point:
#     def __init__(self,x,y): #Constructor
#         self.x=x         #Self to reference the current object
#         self.y=y
#     def move(self):
#         print("Move")

#     def draw(self):
#         print("Draw")

# point1=Point()
# point1.draw()    


# # Constructors
# # A function that gets called at the time of creating an object
# point=Point(10,20)
# print(point.x)

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def talk(self):
#         print(f"Hi, I am {self.name}")

# Bernardine=Person("Bernardine Okrah")
# print(Bernardine.name)
# Bernardine.talk()

# #Inheritance

# class Mammal():
#     def walk(self):
#         print("Lets go for a walk!")

# class Dog(Mammal):
#     def bark(self):
#         print("Bark!")

# class Cat:
#     def be_annoying(self):
#         print('You are annoying')

# dog1=Dog()
# dog1.walk()
# dog1.bark()

# cat1=Cat()
# cat1.be_annoying()

# # Modules
# # Modules are file with python code. Used to organize code into multiple sections

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName=firstName
        self.lastName=lastName
        self.age=age


# course_title='Programming for engineers'
# print(course_title)

        


















