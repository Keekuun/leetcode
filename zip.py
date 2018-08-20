# zip函数：

a = [1, 2, 3]
b = [7, 8, 9, 10]
c = [4, 5, 6]
abc1 = list(zip(a, b, c))  # zip返回值为一个指向运算后各元组的地址，所以转换为list类型；
print(abc1)
print(*abc1)
abc2 = zip(a, b, c)
print(*abc2)
d = zip(*abc1)  # 与zip相反，可以理解为解压，返回值也是地址
print(*d)


# zip函数：

a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7]
ab = zip(a,b)
print(ab)
print(list(ab))
print(*ab)
