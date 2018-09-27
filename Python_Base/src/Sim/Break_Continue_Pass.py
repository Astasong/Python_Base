# _*_coding:utf-8_*_
'''
Created on 2017年8月11日

@author: lenovo
'''
#pass :不做任何事情，只起到占位的作用
#continue: 跳出本次循环
#break：结束循环

#break & continue example
number = 12

while True:
    guess = int(input("please enter a number:"))
    if  guess == number:
        break
    elif guess < number:
        print("No,guess is lower than that,keep guessinng!")
        continue
    else:
        print("No,guess is higher than that,keep guessing!")
        continue
print('Bingo! you guessed it right.')
print('(but you do not win any prizes!)') 
print('Done')


#continue and pass difference

a_list = [0, 1, 2]

print("using continue:")
for i in a_list:
    if not i:
        continue
    print(i)
    
print("using pass:")    
for i in a_list:
    if not i:
        pass
    print(i) 


#pass 表示什么都不干，起到一个占位符的作用
#比如在定义了一个函数，但是函数体的代码实现还不确定，
#但是要保证整个的代码能运行起来，即可使用pass

def xyz():
    pass

def tyl():
    pass

