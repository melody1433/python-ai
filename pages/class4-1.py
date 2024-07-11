i = 0
while i < 10:  # 條件式迴圈,當1<5時執行
    print(i)
    i += 1  # i=i+1


# 算術指定運算子
a = 10
a += 1  # 等同於 a=a+1
print(a)
a -= 1  # 等同於 a=a-1
print(a)
a *= 2  # 等同於 a=a*2
print(a)
a /= 2  # 等同於 a=a/2
print(a)
a //= 2  # 等同於 a=a//2
print(a)
a %= 2  # 等同於 a=a%2
print(a)
a **= 2  # 等同於 a=a**2
print(a)


# 根據以上符號列出優先順序
# 1. ()
# 2. **
# 3. * / // %
# 4. + -
# 5. ==, !=, <, >, <=, >=
# 6. not,and,or
# 7.= += -= *= /= //= %= **=


# break跳出迴圈
i = 1
while i < 10:  # 條件式迴圈,當1<5時執行
    print(i)  # 印出i
    if i == 5:  # 判斷條件
        break  # 當i等於5時跳出迴圈
    i += 1

    for i in range(1, 6):  # for迴圈,i從1開始到5
        print(i)  # 印出i
        if i == 3:
            break  # 當i等於3時跳出迴圈


# random
import random  # 引入random模組

print(random.randrange(10))  # 產生一個0到9的隨機整數
print(random.randint(1, 10))  # 產生一個1到9的整數
print(random.choice(1, 10, 2))  # 產生一個1到9的奇數
# randrange和range一樣，第一個數字為開始，第二個數字為結束，第三個數字為間隔
# 不會數到結束的數字，randrange(1,10)只會從1到9隨機選一個數字


print(random.randint(1, 10))  # 產生一個1到10的整數
# randint和randrange一樣，第一個數字為開始，第二個數字為結束
# 但randint一定要設定兩個數字，且會數到結束的數字
