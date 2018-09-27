'''
Created on 2017年9月8日

@author: lenovo
'''
#Python OO example

class Student:
#    装饰器（相当于java中类的构造器） 其中self相当于this
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def introduce(self):
        print("hi! 我是 " + self.name)
        print("my grade is: " + str(self.grade))
        
    def improve(self, amount):
        self.grade = self.grade + amount

jim = Student("jim", 86)
jim.introduce()

jim.improve(10)
jim.introduce()  