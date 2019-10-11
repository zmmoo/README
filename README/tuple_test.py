info_tuple = ("zhangmeng", 18, 175)
print(type(info_tuple))
# info_tuple[0] = "zm"  不能修改

# 只包含一个数据的元组
tuple_test = ("3",)

tuple_test.count(3)
tuple_test.index("3")


# 通常存储不同类型的数据  多数不使用 for遍历
for i in info_tuple:
    print(i)

# 可以作为函数多个返回值
# 降列表转化成元组 可不被修改

print("%s 年龄是 %d 身高 %d" % info_tuple)

info_str = "%s 年龄是 %d 身高 %d" % info_tuple        #  sprintf()
print(info_str)

print(list(info_str))

list_test = [1, 2, 3, 4]
list_test = tuple(list_test)
print(list_test)
list_test[0] = 9 # 不能修改
print(list_test)





