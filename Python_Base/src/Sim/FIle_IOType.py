#_*_coding:utf-8_*_

'''
Created on 2017年8月16日

@author: lenovo
'''
#1. 写出文件
#2. 读入文件

#Code:

some_sentences = '''\
I love learning python
because python is fun
and also easy to use
'''

#Open for 'w'irting
f = open('sentences.txt', 'w')
#Write text to File
f.write(some_sentences)
f.close()

#If not specifying mode, 'r'ead mode is default
f = open('sentences.txt')
while True:
    line = f.readline()
    #Zero length means End Of File
    if len(line) == 0:
        break
    print(line) 
# close the File
f.close

#文件传输流都是使用open函数来进行操作的
