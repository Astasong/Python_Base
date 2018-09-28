'''
Created on 2017年9月8日

@author: lenovo
'''

#except example
#print(8/0)

#print(hello * 4)

#num = 6
#print("hello world" + num)

#handling except
while True:
    try:
        x = int(input("Please enter a number"))
        break
    except ValueError:
        print("Not valid input, try again...")
#the first
#the two
#the three