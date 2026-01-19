# 序列相加 操作符重载：Python 的 * 操作符很聪明。如果两边都是数字，它执行乘法；如果一边是字符串而另一边是整数，它就自动切换到“重复”模式。
# list1 = [10, 20, 30, 40]
# list2 = [50, 60, 70, 80]
# list3 = list1 + list2
# print(list3)

# tuple1 = (10, 20, 30, 40)
# tuple2 = (50, 60, 70, 80)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# str1 = 'hello'
# str2 = 'atguigu'
# str3 = str1 + str2
# print(str3)

# 错误示例
# list1 = [10, 20, 30, 40]
# str1 = 'hello'
# print(list1 + str1)

# 序列相乘（重复）
# list1 = [10, 20, 30, 40]
# list2 = list1 * 3
# print(list2)

# tuple1 = (10, 20, 30, 40)
# tuple2 = tuple1 * 3
# print(tuple2)

str1 = 'hello'
str2 = str1 * 6
print(str2)

