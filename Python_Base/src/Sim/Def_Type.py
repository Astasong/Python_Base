
#-*- coding: utf-8 -*-
'''
Created on 2017年8月11日

@author: lenovo
'''



#Python 中使用def +函数名称（函数参数列表）： 来表示  
# 表示程序中可重复使用的程序块

#没有参数 也没有返回值
def sayhi():
    print("hi")
sayhi()

#有参数 没有返回值
def print_sum_two(a,b):
    c = a + b
    print(c)
print_sum_two(3, 6)

#参数中传入一个字符串
def hello_str(str):
    print("hello "+str)
hello_str("china")
hello_str("Python")

 
#有参数，有返回值
def repeat_str(str, times):
    repeated_strs = str * times
    return repeated_strs
 
 
repeated_strings = repeat_str("Happy Birthday!", 4)
print(repeated_strings)


#全局变量 和 局部变量
#全局变量作用范围 是作用于整个全局范围 
#局部变量作用范围 是作用于内部的 出去后就不再作用了 eg：函数内部的局部变量
x = 60
 
def foo(x):
    print("x is: " + str(x))
    x = 3
    print("change local x to " + str(x))
 
foo(x)
print('x is still', str(x))



x = 60
 
def fooo():
    global x #将x定义为全局变量 方法内部改变x值后 在外部生效
    print("x is: " + str(x))
    x = 3
    print("change local x to " + str(x))
 
fooo()
print('value of x is' , str(x))

