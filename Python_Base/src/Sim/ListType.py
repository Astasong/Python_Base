#_*_coding:utf-8_*_

'''
Created on aug 9 2017
@author: lenovo
'''
#����һ���б�
number_list=[1,2,3,7]

#�޸��б��еĶ�Ӧ��ֵ
number_list[1]=30
print(str(number_list))

#ɾ���б��е�ĳһ��
del number_list[0]
print(str(number_list))

#��ȡ�б�ĳ���
print(len(number_list))
print(len([1,2,3,4]))

#�б�����
print([1,2,3]+[4,5,6])
numberCop_list=[1,2,3]+[4,5,6]
print(len(numberCop_list))

print(len([1,2,3]*4))
print(str([1,2,3]*4))
#������Խ�縳ֵ���б��е������list assignment index out of range
#numberCop_list[6]=7
#print(str(numberCop_list))

print(3 in [1,2,3])

#�б�Ľ�ȡ
abcd_list =['a', 'b', 'c', 'd'] 
print(abcd_list[1])
print(abcd_list[-1])
#��ȡ��ʱ��[1:3]��ʾ��ȡ[1,3)
print(abcd_list[1:3])

#�б�����ֵ����Сֵ
print(max(numberCop_list))
print(min(numberCop_list))

#list.index(obj)�����б����ҳ�ĳ��ֵ��һ��ƥ���������λ��
print(numberCop_list.index(6))

#list.remove(obj)���Ƴ��б���ĳ��ֵ�ĵ�һ��ƥ���� ����ֵ��None
print(numberCop_list.remove(3))

print(numberCop_list)

#list.count(obj)��ͳ��ĳ��Ԫ�����б��г��ֵĴ���
print(numberCop_list.count(2))

#list.append(obj)�����б�ĩβ����µĶ���
numberCop_list.append(2)

print(numberCop_list.count(2))

print(numberCop_list)

#list.reverse()�������б���Ԫ��
print(numberCop_list.reverse())
print(numberCop_list)

#list.sort([func])����ԭ�б��������
print(numberCop_list.sort())
print(numberCop_list)

print(numberCop_list.count(2))
