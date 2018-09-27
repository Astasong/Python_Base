#_*_coding:utf-8_*_
'''
Created on 2017年8月11日

@author: lenovo
'''

#使用Python来实现一个冒泡程序
array = [2,4,3,6,1,9,7]

for i  in range(0,len(array)-1,1):
    for j in range(0,len(array)-i-1):
        if array[j] > array[j+1]:
            tem = array[j]
            array[j]=array[j+1]
            array[j+1]=tem
print(str(array))
