import streamlit as st

with st.expander("class1程式筆記"):
    st.markdown(
        """
    # Python 程式筆記

```python
    # 註解筆記
    # 代表註解的行
    '''
    這是多行註解
    '''

    # 單行註解
    print("123")  # 整數
    print("123.456")  # 浮點數
    print("hello")  # 字串
    print("true")  # 布林值
    print("false")  # 布林值
    print('"')  # 印出雙引號
    print("'")  # 印出單引號

    # 變數與資料型別
    a = 10  # 整數
    print(a)
    b = "hello"  # 字串
    print(b)

    # 算術運算
    print(1 + 1)  # 加法計算
    print(2 - 1)  # 減法計算
    print(1 * 1)  # 乘法計算
    print(6 / 2)  # 除法計算
    print(3 // 2)  # 整數除法計算
    print(3 % 2)  # 取於數計算
    print(3 ** 2)  # 指數計算

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
    print(a + " " + b * 3)  # 加法乘法混和

    # 字串格式化
    print(f"hello {b}")

    # 字串操作
    print(len("hello"))  # 字串長度
    print(int("123"))  # 字串轉整數
    print(float("123.456"))  # 字串轉浮點數
    print(str(123))  # 整數轉字串
    print(bool(1))  # 整數轉布林值

    # 輸入與輸出
    a = input("在這邊可以開始輸入文字:")
    print(f"你輸入的是 {a}")  # 印出輸入的文字
    print(f"input()輸入的內容型態是 {type(a)}")  # 印出輸入的內容型態是字串

    # 計算正方形面積
    a = input("輸入正方形的邊長:")
    area = int(a) ** 2
    print(f"正方形的面積是 {area}")
```

    """
    )

with st.expander("class2程式筆記"):
    st.markdown(
        """
    
### 比較運算

```python
print(1 == 1)  # 這是比較是否相等的運算
print(1 != 1)  # 這是比較是否不相等的運算
print(1 < 1)   # 這是比較是否小於的運算
print(1 > 1)   # 這是比較是否大於的運算
print(1 <= 1)  # 這是比較是否小於或等於的運算
print(1 >= 1)  # 這是比較是否大於或等於的運算
```

### 邏輯運算

```python
print(not True)       # 這是相反的運算
print(not False)      # 這是相反的運算
print(True and True)  # 這是全部要符合條件才算true
print(True and False) # 這是全部要符合條件才算true
print(False and False)# 這是全部要符合條件才算true
print(True or True)   # 這是其中一個符合條件就算true
print(True or False)  # 這是其中一個符合條件就算true
print(False or False) # 這是其中一個符合條件就算true
```

### 運算符優先順序

```python
# 1. ()
# 2. **
# 3. * / // %
# 4. + -
# 5. ==, !=, <, >, <=, >=
# 6. not, and, or
```

### if-else 判斷

```python
password = input("請輸入密碼：")
if password == "123456":
    print("密碼正確")
elif password == "12345678":
    print("密碼正確")
else:
    print("密碼錯誤")
```

`if` 和 `elif` 判斷密碼是否正確。

### Streamlit 應用

```python
import streamlit as st

number = st.number_input("請輸入數字", step=1)
st.markdown(f"你輸入的數字是{number}")

st.title("練習")

number = st.number_input("請輸入分數", step=1, min_value=0, max_value=100)
st.markdown(f"你輸入的分數是{number}")
if number >= 90:
    st.markdown("你得到了A分")
elif number >= 80:
    st.markdown("你得到了B分")
elif number >= 70:
    st.markdown("你得到了C分")
elif number >= 60:
    st.markdown("你得到了D分")
else:
    st.markdown("你得到了F分")
```

這段程式使用了 Streamlit 來實現數字和分數的輸入及顯示。

### 按鈕練習

```python
st.title("按鈕練習")
st.button("點我", key="button")
if st.button("點我", key="button2"):
    st.balloons()
```

### for 迴圈

```python
for i in range(10):  # 這是循環的變數
    print(i)  # 每次只從range(10)取出一個數字,是從0到9

for i in range(2, 100):  # range(2,100)是從2到99的數字
    print(i)  # 每次只從range(2,100)取出一個數字,是從2到99

for i in range(2, 100, 2):  # range(2,100,2)是從2到99的數字,每次取出的數字是2的倍數
    print(i)  # 每次只從range(2,100,2)取出一個數字,是從2到99的偶數

for i in range(100, 3, -2):  # range(100,3,-2)是從100到4的數字,每次取出的數字是偶數
    print(i)  # 每次只從range(100,3,-2)取出一個數字,是從100到4的偶數
```

這段程式展示了 for 迴圈的多種用法，包括不同範圍和步長的設定。

### Streamlit 數字和箭頭金字塔

```python
import streamlit as st

st.title("數字金字塔")
number = st.number_input("請輸入數字", step=1, min_value=0, max_value=9)
for i in range(0, number + 1):
    st.markdown(str(i) * i)

st.title("箭頭金字塔")
number = st.number_input("請輸入數字", step=1, min_value=1)  # 幾層
arrow = ""
for i in range(1, number * 2, 2):  # 奇數
    arrow += " " * ((number * 2 - i) // 2) + "*" * i + "\n"
for i in range(number):
    arrow += " " * (number - 1) + "*" + "\n"
st.markdown(
    f'''
```\n箭頭金字塔:\n{arrow}\n```
'''
)
```

這段程式使用 Streamlit 創建數字金字塔和箭頭金字塔。

### List 操作

```python
print([])  # 這是一個空的list
print([1, 2, 3])  # 這是一個有三個元素的list
L = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
print(L[0])  # 取出L中第一個元素,元素編號是從0開始
print(L[1])  # 取出L中第二個元素
print(L[2])  # 取出L中第三個元素

for i in range(len(L)):
    print(L[i])  # 取出L中第i個元素

for abc in L:
    print(abc)  # 取出L中的所有元素

L[0] = "abc"  # 把L中第一個元素改成"abc"
```

    """
    )
