#_*_coding:utf-8_*_

'''
Created on aug 9 2017
@author: lenovo
'''
#创建一个列表
number_list=[1,2,3,7]

#修改列表中的对应项值
number_list[1]=30
print(str(number_list))

#删除列表中的某一项
del number_list[0]
print(str(number_list))

#获取列表的长度
print(len(number_list))
print(len([1,2,3,4]))

#列表的组合
print([1,2,3]+[4,5,6])
numberCop_list=[1,2,3]+[4,5,6]
print(len(numberCop_list))

print(len([1,2,3]*4))
print(str([1,2,3]*4))
#不可以越界赋值给列表中的项，否则list assignment index out of range
#numberCop_list[6]=7
#print(str(numberCop_list))

print(3 in [1,2,3])

#列表的截取
abcd_list =['a', 'b', 'c', 'd'] 
print(abcd_list[1])
print(abcd_list[-1])
#截取的时候[1:3]表示截取[1,3)
print(abcd_list[1:3])

#列表的最大值、最小值
print(max(numberCop_list))
print(min(numberCop_list))

#list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
print(numberCop_list.index(6))

#list.remove(obj)：移除列表中某个值的第一个匹配项 返回值是None
print(numberCop_list.remove(3))

print(numberCop_list)

#list.count(obj)：统计某个元素在列表中出现的次数
print(numberCop_list.count(2))

#list.append(obj)：在列表末尾添加新的对象
numberCop_list.append(2)

print(numberCop_list.count(2))

print(numberCop_list)

#list.reverse()：反向列表中元素
print(numberCop_list.reverse())
print(numberCop_list)

#list.sort([func])：对原列表进行排序
print(numberCop_list.sort())
print(numberCop_list)

print(numberCop_list.count(2))
