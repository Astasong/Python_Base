
'''
Created on 2017年8月10日

@author: lenovo
'''

print("哈哈")
#创建一个词典 {key1:value1,key2:value2……}
phone_book = {'Tom': 123, "Jerry": 456, 'Kim': 789}

mixed_dict = {"Tom": 'boy', 11: 23.5}

#访问字典中的具体一项时 使用phone_book["Kim"]：表示键Kim所对应的值
print("kim's number is  "+str(phone_book["Kim"]))
print("Tom is a "+mixed_dict["Tom"])

#修改字典中某一项
mixed_dict["Tom"] = "girl"
print("Tom is a "+mixed_dict["Tom"])

#update 方法：在字典后面追加
mixed_dict.update({"sim":"boy",12:23})
print(str(mixed_dict))

#del 删除字典中的某一项
del mixed_dict["Tom"]
print(str(mixed_dict))

#clear方法 清空字典  清空的是字典里面的内容
mixed_dict.clear()
print(str(mixed_dict))


#删除词典元素以及词典本身
del phone_book
#彻底删除了 phone_book的全部内容以及字典的名称 所以删除的字典已经不存在了 

#print(str(phone_book)) 这里打印会报错 因为该字典已经是不存在的了  name 'phone_book' is not defined

#字典里面不允许同一个键出现两次，若出现则最后一个会相同键的value会覆盖前面所有相同键的value
rep_test = {'Name': 'aa', 'age':5, 'Name': 'bb'}
print("rep_test: " + str(rep_test))

print(type(rep_test))

