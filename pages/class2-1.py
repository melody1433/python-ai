print(1 == 1)  # 這是比較是否相等的運算
print(1 != 1)  # 這是比較是否不相等的運算
print(1 < 1)  # 這是比較是否小於的運算
print(1 > 1)  # 這是比較是否大於的運算
print(1 <= 1)  # 這是比較是否小於或等於的運算
print(1 >= 1)  # 這是比較是否大於或等於的運算


print(not True)  # 這是相反的運算
print(not False)  # 這是相反的運算

print(True and True)  # 這是全部要符合條件才算true
print(True and False)  # 這是全部要符合條件才算true
print(False and False)  # 這是全部要符合條件才算true

print(True or True)  # 這是其中一個符合條件就算true
print(True or False)  # 這是其中一個符合條件就算true
print(False or False)  # 這是其中一個符合條件就算true


# 根據以上符號列出優先順序
# 1. ()
# 2. **
# 3. * / // %
# 4. + -
# 5. ==, !=, <, >, <=, >=
# 6. not,and,or


password = input("請輸入密碼：")
if password == "123456":
    print("密碼正確")
elif password == "12345678":
    print("密碼正確")
else:
    print("密碼錯誤")

# 判斷一定要是if開頭,if只能有一個
# 判斷可以有無限個elif,也可以沒有
# 判斷可以有一個else,也可以沒有
# elif和else都是選擇性的
