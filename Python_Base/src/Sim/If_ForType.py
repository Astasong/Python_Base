# _*_coding:utf-8_*_
'''
Created on 2017年8月11日

@author: lenovo
'''

#if statement example
 
number = 59
#从键盘键入一个值input(提示信息)
guess = int(input('Enter an integer : '))
 
if guess == number:
# New block starts here
    print('Bingo! you guessed it right.')
    print('(but you do not win any prizes!)')
# New block ends here
elif guess < number:
# Another block
    print('No, the number is higher than that')
# You can do whatever you want in a block ...
else:
    print('No, the number is a  lower than that')
# you must have guessed > number to reach here

print('Done')
# This last statement is always executed,
# after the if statement is executed.


#the for loop example

for i in range(1, 10):
    print(i)
else:
    print('The for loop is over')
     
     
a_list = [1, 3, 5, 7, 9]
for i in a_list:
    print(i)
 
a_tuple = (1, 3, 5, 7, 9)
for i in a_tuple:
    print(i)
     
a_dict = {'Tom':'111', 'Jerry':'222', 'Cathy':'333'}
for ele in a_dict:
    print(ele) #ele指的是字典中的键
    print(a_dict[ele])
     
for key, elem in a_dict.items():
    print(key, elem)

