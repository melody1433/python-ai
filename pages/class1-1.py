# 註解筆記
# 代表註解的行
"""
這是多行註解
"""
# print("hello")# ctrl+?可以單行註解


print("123")  # 整數
print("123.456")  # 浮點數
print("hello")  # 字串
print("true")  # 布林值
print("false")  # 布林值
print('"')  # 印出雙引號
print("'")  # 印出單引號


a = 10  # 把10存入變數a的空間,=就是將右邊的值存到左邊的空間
print(a)
b = "hello"  # 把hello存入變數b的空間
print(b)


print(1 + 1)  # 加法計算
print(2 - 1)  # 減法計算
print(1 * 1)  # 乘法計算
print(6 / 2)  # 除法計算
print(3 // 2)  # 整數除法計算
print(3 % 2)  # 取於數計算
print(3**2)  # 指數計算


# 符號的優先順序
# 1. ()
# 2. **
# 3. * / // %
# 4. + -


# 字串運算
a = "hello"
b = "world"
print(a + b)  # 字串加法
print(a + " " + b)  # 字串加法
print(a * 3)  # 字串重複
# 加法乘法混和
print(a + " " + b * 3)


print(f"hello {b}")
# f是字串格式化,可以在字串中加入變數,用{}包住變數


print(len("hello"))  # 字串長度
print(int("123"))  # 字串轉整數
print(float("123.456"))  # 字串轉浮點數
print(str(123))  # 整數轉字串
print(bool(1))  # 整數轉布林值


print("input()可以在終端機輸入文字")
a = input("在這邊可以開始輸入文字")
print(f"你輸入的是{a}")  # 印出輸入的文字
print(f"input()輸入的內容型態是{type(a)}")  # 印出輸入的內容型態是字串


#  計算正方形面積
a = input("輸入正方形的邊長:")
area = int(a) ** 2
print(f"正方形的面積是{area}")
