# def addition(x,y):
#     z=x +y
#     return f"sum={z}"


# print(addition(2,4))


# def addition(*x):
#     print(x)
#     print(type(x))

# addition(1,2,3,4,5,6,7)


# class BakingPan:
#     pass

# bread1=BakingPan()
# bread1.flour='Soft'
# bread1.sugar=20
# bread1.special_ingredient='Wheat'
# print(bread1.flour)


# bread2=BakingPan()
# bread2.flour='Hard'
# bread2.sugar=10
# bread2.special_ingredient='coconut'
# print(bread2.special_ingredient)

# school='University of Ghana'



# class BakingPan:
#     unit_price=5
#     def __init__(self,flour, sugar, special_ingredient):
#         self.flour=flour
#         self.sugar=sugar
#         self.special_ingredient=special_ingredient



#     def bread_name(self):
#         return f'{self.special_ingredient} bread'
    
#     def total_price(self,quantity):
#         total=quantity*self.unit_price
#         return f'Total Price = GhC{total}'

# bread1=BakingPan('Soft',20,'coconut')
# bread2=BakingPan('Hard',10,'Banana')
# print(bread1.total_price(5))


# print(BakingPan.department)
# print(bread1.department)


#Student MIS
# class Person:
#     def __init__(self,firstName,lastName,age):
#         self.firstName=firstName
#         self.lastName=lastName
#         self.age=age
#         self.email=f'{firstName[0]}.{self.lastName}@st.ug.edu.gh'.lower()

#     def fullName(self):
#         return f'{self.firstName} {self.lastName}'
    
#     def name_initials(self):
#         return f'{self.firstName[0]}.{self.lastName[0]}'



# person1=Person('Bernardine','Adusei',20)
# # print(person1.name_initials())

# person2=Person('Mary','Blige',21)
# # print(person2.email)

# #Section2
# class Student(Person):
#     def __init__(self, firstName, lastName, age, hall, courses=None):
#         super().__init__(firstName, lastName, age)
#         self.hall = hall
#         if courses is None:
#             self.courses = []
#         else:
#             self.courses = courses

#     def add_course(self, course_title):
#         if course_title not in self.courses:
#             self.courses.append(course_title)

#     def drop_course(self, course_title):
#         if course_title in self.courses:
#             self.courses.remove(course_title)

#     def print_all_courses(self):
#         print(f'{self.fullName()} has registered {len(self.courses)} courses')
#         print('-' * 30)
#         for course in self.courses:
#             print(course)


# student1 = Student('Joana', 'Jones', 19, 'Mensah Sarbah')
# student1.add_course('Python')
# student1.add_course('Java')
# student1.add_course('African Studies')
# student1.add_course('Project work')

# print(student1.courses)
# student1.print_all_courses()


#Python modules
#Inbuilt modules
# from getpass import getpass
# from keyword import kwlist
# from math import pi,prod

# print(pi)
# pin=getpass('Enter your pin: ')
# print(f'You entered: {pin}')

#Custom Modules
# from Study import course_title
# print(course_title)

# import Study as st
 # print(st.course_title)

# person1=st.Person('Haqq','Basit',19)
# print(person1.firstName)

#Libraries
# import folium
# myMap=folium.Map()
# myMap.save=('map.html')

import pyttsx3
speaker=pyttsx3.init()
speaker.say('My name is Bernardine. My full name is Bernardine Adusei-Okrah')
speaker.runAndWait()



























