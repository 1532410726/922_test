#常用数据结构列表
# 相同点
# 都是有序的
# 都是异构的，能够包含不同类型的对象
# 都支持索引和切片
# 区别
# 声明方式不同，元组使用()，列表使用 []
# 列表是可变的，元组是不可变的
li1 = [1,2,3,4,5,"wang","bin","bin"]
li2 = [6,7,8,9]
print(type(li1),li1)
print(li1[0:5])
print(li1[-3])
li3 = li1+li2
print(li3)

#in：检查一个对象是否在列表中，如果在则返回 True，否则返回 False；not in：
# 检查一个列表是否不包含某个元素。如果不在返回 True，否则返回 False。
print(10 in li3,1 in  li3)
print(10 not in li3)

#append(item)：将一个对象 item 添加到列表的末尾。
li1.append("dahsuaige")
print(li1)

#定义一个元组
t1 = (1,2,3)
print(type(t1),t1)

# 字典是无序的键值对集合
# 字典用大括号{}包围
# 每个键/值对之间用一个逗号分隔
# 各个键与值之间用一个冒号分隔
# 字典是动态的
di = {"name1": "wang", "name2": "bin", "name3": "bin", "zhangxiang": "shuaide"}
print(type(di), di)

#keys(),返回由字典键组成的一个新视图对象。
# for key in di:
#     print(str(key))

#values(),返回由字典值组成的一个新视图对象。
# values = di.values()
# print(values)
for value in di.values():
    print(value)

#items(),返回由字典项 ((键, 值) 对) 组成的一个新视图对象。
items1 = di.items()
#print(items1)
for items in di.items():
    print(items)

#get(key),获取指定 key 关联的 value 值;  此方法的好处是无需担心 key 是否存在，永远都不会引发 KeyError 错误。
xing = di.get("name1")
print(xing)

#update(dict),使用来自 dict 的键/值对更新字典，覆盖原有的键和值。
di.update({"name2" : "bing", "name3" : "bing"})
print(di)


"""
给定一个字典对象，请使用字典推导式，将它的key和value分别进行交换。也就是key变成值，值变成key。

输入: {'a': 1, 'b': 2, 'c': 3}
输出: {1: 'a', 2: 'b', 3: 'c'}
"""
d2 = {'a': 1, 'b': 2, 'c': 3}
for key in d2.keys():
    for valus in d2.values():
        for items in valus,key:
 print(type(items))
















