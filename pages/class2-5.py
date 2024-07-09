print[]# 這是一個空的list
print[1,2,3]# 這是一個有三個元素的list
L=["a","b","c","d","e","f","g","h","i",]
print(L[0])# 取出L中第一個元素,元素編號是從0開始
print(L[1])# 取出L中第二個元素
print(L[2])# 取出L中第三個元素

for i in range(len(L)):
    print(L[i])#取出L中第i個元素

for abc in L:
 print(abc)# 取出L中的所有元素
 

 L[0]="abc"# 把L中第一個元素改成"abc"
