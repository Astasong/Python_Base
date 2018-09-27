# _*_coding:utf-8_*_

'''
Created on 2017年8月11日

@author: lenovo
'''
#while 语句
from setuptools.command.build_ext import if_dl


number = 76
guess_flag = False

while guess_flag == False:
    guess = int(input("enter an integer "))
    if guess == number:
        guess_flag = True
    elif guess < number:
        print("No, the number is higher than that, keep guessing")
    else:
        print("No,the number is a lower than that,keep guessing")
print("Bingo! you guess it right!")
print("but you do not win any prizes")
print("done")


#for 语句
num_chance=3
print("you have only three times guess")

for guess_chance in range (1,num_chance+1):
    print("guess"+str(guess_chance))
    guess = int(input("enter an integer:"))
    if guess == number:
        print('Bingo! you guessed it right.')
        print('(but you do not win any prizes!)') 
        break
    elif guess > number:
        print("No,  the number is lower than that, keep guessing, you have"  + str(num_chance - guess_chance) + "chances left")
        
    else :
        print("No, the number is higher than that,keep guessing, you have " + str(num_chance - guess_chance) + "chances left")
print("done")


