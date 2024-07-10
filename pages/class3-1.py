i = [1, 2, 3]
i.append(4)
print(i)


j = [1, 2, 3, 4, 5]
j.remove(3)
print(j)


o = [9, 1, -4, 3, 7, 11, 3]  # 這是一個有7個元素的list
print(o.count(3))  # 計算o中有多少個是3
for i in range(o):
    o.remove(3)  # o中的3移除
print(o)  # 印出


p = [1, 2, 3]
p.pop(0)  # 刪除p中第一個元素
print(p)  # 印出
# pop與remove的差別,pop是用index,remove是用元素來刪除


l = [3, 1, 5, 4, 2]
l.sort()  # 把l中的元素排序
print(l)  # 印出
l.reverse()  # 把l中的元素由大排到小
print(l)  # 印出


m = [3, 1, 5, 4, 2]
print(m.index(3))  # 找出m中3的index
