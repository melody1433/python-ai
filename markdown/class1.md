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
