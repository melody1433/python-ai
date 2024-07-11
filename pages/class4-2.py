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
