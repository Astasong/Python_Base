# _*_coding:utf-8_*_
'''
Created on 2017年8月11日

@author: lenovo
'''
#函数的默认参数的使用 在函数调用的时候可以不写 即为默认参数的值
def repeated_str(s,time=2):
    repeated_strs = s * time
    return repeated_strs

print(repeated_str("china "))
#也可以修改 默认参数的值
print(repeated_str("china ", 3))

#不能在有默认参数后面跟随没有默认参数
#def test(a=1,b=2,c):
#    c=3
#    sum=a+b+c
#    print(str(sum))


#下面在有默认参数后面跟随没有默认参数
#test(a=1,b=3,c)     #error_Info:non-default argument follows default argument
    
    
#关键字参数: 调用函数时，选择性的传入部分参数
def func(a, b = 4, c = 8):
    print('a is', a, 'and b is', b, 'and c is', c)

func(13, 17)
func(125, c = 24)
func(c = 40, a = 80)


#VarArgs参数
def print_paras(fpara, *nums, **words):
    print("fpara: " + str(fpara))
    print("nums: " + str(nums))
    print("words: " + str(words)) 
          
print_paras("hello", 1, 3, 5, 7, word = "python", anohter_word = "java")    
