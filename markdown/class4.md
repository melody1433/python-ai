1. **條件式迴圈與算術指定運算子**：

```python
i = 0
while i < 10:  # 條件式迴圈,當1<10時執行
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
```

2. **運算符號優先順序**：
   - 1. ()
   - 2. **
   - 3. * / // %
   - 4. + -
   - 5. ==, !=, <, >, <=, >=
   - 6. not, and, or
   - 7. =, +=, -=, *=, /=, //=, %=, **=

3. **使用break跳出迴圈**：

```python
i = 1
while i < 10:  # 條件式迴圈,當1<10時執行
    print(i)  # 印出i
    if i == 5:  # 判斷條件
        break  # 當i等於5時跳出迴圈
    i += 1

for i in range(1, 6):  # for迴圈,i從1開始到5
    print(i)  # 印出i
    if i == 3:
        break  # 當i等於3時跳出迴圈
```

4. **使用random模組生成隨機數**：

```python
import random  # 引入random模組

print(random.randrange(10))  # 產生一個0到9的隨機整數
print(random.randint(1, 10))  # 產生一個1到10的整數
print(random.choice([1, 3, 5, 7, 9]))  # 產生一個1到9的奇數
```

5. **猜數字遊戲**：

```python
import random  # 引入random模組

number = random.randint(1, 100)  # 產生一個1到100的整數
while True:  # while循環
    guess = int(input("請輸入你的猜測："))  # 輸入猜測
    if guess < 1 or guess > 100:  # 判斷條件
        print("請輸入1到100之間的數字。")  # 印出訊息
    elif guess < number:
        print("太小了，再猜大一點！")
    elif guess > number:
        print("太大了，再猜小一點！")
    else:
        print(f"恭喜你！你猜對了，這個數字是 {number}！")
        break
```

6. **字典操作**：

```python
# 建立字典
d = {"書名": "蘋果", "作者": "香蕉"}

# 讀取字典
print(d["書名"])  # 蘋果

# 字典走訪
for key in d:  # 獲得key
    print(key, d[key])
for key in d.keys():  # 使用keys()取得key
    print(key)
for value in d.values():  # 取得所有的value
    print(value)
for key, value in d.items():  # 取得所有的key, value
    print(f"key={key}, value={value}")
for item in d.items():  # 取得所有的key, value
    print(f"key={item[0]}, value={item[1]}")

# 元素新增/修改
d["書名"] = "蘋果樹"
d["出版商"] = "某某出版社"
print(d)

# 檢查字典是否存在key或value
print("書名" in d)  # True
print("書名2" in d)  # False
print("香蕉" in d.values())  # True
print("蘋果" in d.values())  # False

# 刪除元素
d.pop("書名")  # 刪除key=書名的元素
print(d)
print(d.pop("橘子", "找不到"))  # 如果刪除元素可能不存在
```

7. **Streamlit顯示圖片**：

```python
import streamlit as st
import os

st.title("圖片元件")
image_folder = "image"  # 資料夾名稱
image_files = os.listdir(image_folder)  # 取得資料夾下所有檔案
st.write(image_files)  # 顯示所有檔案

image_size = st.number_input(
    "圖片大小", min_value=50, max_value=500, step=50, value=100
)
# 使用者輸入圖片大小,最小50,最大500,每次增加50

for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", width=image_size)
    # 顯示圖片,根據使用者輸入的大小調整寬度

for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", use_column_width=True)
    # 顯示圖片,使用欄寬度
```
